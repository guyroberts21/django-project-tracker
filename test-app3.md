## Create Dockerfile that pulls the 

```bash
FROM registry.access.redhat.com/rhel7:latest

# Set environment variables to avoid user prompts during package install
ENV TERM=xterm \
    LANG=en_US.UTF-8

# Install dependencies
RUN yum -y update && \
    yum -y install \
        openssl \
        git \
        openssh-clients \
        wget \
        tar \
        expect && \
    yum clean all

# Install mkpasswd from expect package
# (mkpasswd is part of 'expect' in RHEL7)

# Install OpenShift CLI (oc)
RUN wget https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz && \
    tar -xvf oc.tar.gz && \
    mv oc /usr/local/bin/ && \
    chmod +x /usr/local/bin/oc && \
    rm oc.tar.gz

WORKDIR /app
```

## Machine Config Template 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: core-user-password
spec:
  config:
    ignition:
      version: 3.2.0
    passwd:
      users:
        - name: core
          passwordHash: "{{HASH_PLACEHOLDER}}"
```

## GitLab CI Pipeline

```yaml
stages:
  - generate-hash
  - commit-config

variables:
  MACHINE_CONFIG_FILE: "machineconfig-generated.yaml"

generate_password_hash:
  stage: generate-hash
  image: 
    name: your-custom-image:latest  # Use your Docker image (if needed)
    entrypoint: [""]
  script:
    # Fetch password from CSM (replace with your CSM CLI command)
    - PASSWORD=$(csm-cli get-secret master-secret --field=password)
    
    # Generate SHA-512 hash (using mkpasswd)
    - HASH=$(mkpasswd --method=SHA-512 -S "somesalt" $PASSWORD)
    
    # Replace placeholder in template
    - sed "s|{{HASH_PLACEHOLDER}}|$HASH|g" machineconfig-template.yaml > $MACHINE_CONFIG_FILE
    
    # Save the hash as an artifact for the next stage
    - echo $HASH > hash.txt
  artifacts:
    paths:
      - $MACHINE_CONFIG_FILE
      - hash.txt
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"  # Run on a schedule or manually

commit_machineconfig:
  stage: commit-config
  image: alpine:latest
  before_script:
    - apk add --no-cache git openssh-client
    # Configure Git user
    - git config --global user.email "gitlab-ci@example.com"
    - git config --global user.name "GitLab CI"
    # Add Git server SSH fingerprint (replace with your server's)
    - mkdir -p ~/.ssh
    - echo "github.com ssh-ed25519 AAAAC3..." >> ~/.ssh/known_hosts
  script:
    # Clone the repository
    - git clone git@github.com:your-org/your-repo.git
    - cd your-repo
    
    # Copy the generated MachineConfig
    - cp ../$MACHINE_CONFIG_FILE ./machineconfigs/
    
    # Commit and push
    - git add ./machineconfigs/$MACHINE_CONFIG_FILE
    - git commit -m "Update core user password hash [skip ci]"
    - git push origin main
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
```


```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: set-core-password-from-etcdsecret
spec:
  config:
    ignition:
      version: 3.2.0
    systemd:
      units:
      - name: set-core-password.service
        enabled: true
        contents: |
          [Unit]
          Description=Fetch hashed core password from etcdsecret and apply
          After=network-online.target kubelet.service
          Wants=network-online.target

          [Service]
          Type=oneshot
          RemainAfterExit=yes
          Environment="KUBECONFIG=/etc/kubernetes/kubeconfig"
          ExecStart=/bin/bash -eux -c '\
            # pull the base64-encoded hash out of the Secret \
            HASH_B64=$(oc get secret etcdsecret \
                        -n openshift-config \
                        -o jsonpath="{.data.password}"); \
            # decode to get the actual hashed password string \
            HASH=$(echo "${HASH_B64}" | base64 -d); \
            # apply it to core, treating HASH as an already-hashed password \
            echo "core:${HASH}" | chpasswd -e \
          '

          [Install]
          WantedBy=multi-user.target
```
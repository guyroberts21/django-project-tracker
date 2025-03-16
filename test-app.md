Below is a draft document that explains the fix and answers your three questions. You can adjust the wording as needed for your internal documentation.

--- 

# Document: Preparing for the OpenShift 4.13 Upgrade – SSH Configuration Fix

**Purpose:**  
This document provides a detailed explanation of the required SSH configuration changes when upgrading from OpenShift 4.12 to 4.13+ and outlines the actions, backup/rollback plan, and testing methodology to ensure that the fix works as expected.

---

## Background

With the introduction of a RHEL 9.2–based RHCOS in OpenShift 4.13, the default SSH key location has changed. Previously, SSH keys were located in:
```
/home/core/.ssh/authorized_keys
```
Now, they reside in:
```
/home/core/.ssh/authorized_keys.d/ignition
```
This change means that any customizations made to the SSH server configuration file (`/etc/ssh/sshd_config`) on your nodes must be adjusted. Red Hat’s recommended solution is to include the line:
```
Include /etc/ssh/sshd_config.d/*.conf
```
at the top of the `/etc/ssh/sshd_config` file. Alternatively, you may move your custom configurations to a separate file within `/etc/ssh/sshd_config.d/` and revert changes in the main configuration file.

---

## Q1: What actions can we take before proceeding to the 4.13 upgrade?

### **Pre-Upgrade Actions**

1. **Audit Your Current SSH Configuration:**
   - **Review Customizations:**  
     Check whether `/etc/ssh/sshd_config` has been modified from its default state. Look for any custom directives that might conflict with the new requirements.
   - **Verify Inclusion:**  
     Confirm if the configuration already contains the line:
     ```bash
     Include /etc/ssh/sshd_config.d/*.conf
     ```
     If not, plan to add it.

2. **Prepare the Necessary Directory and File:**
   - **Create the Directory:**  
     On each node (or via a MachineConfig resource), create the directory that OpenShift now expects:
     ```bash
     mkdir -p /etc/ssh/sshd_config.d
     ```
   - **Create an Empty Include File:**  
     Place an empty file in the directory to ensure that the inclusion directive does not result in errors:
     ```bash
     touch /etc/ssh/sshd_config.d/empty_include.conf
     ```
   - **MachineConfig Approach:**  
     If you are using MachineConfigs for configuration management, create a MachineConfig resource that performs these steps on all nodes before the upgrade. This ensures that even nodes where `/etc/ssh/sshd_config` has been customized will include the proper directory and file.

3. **Document and Communicate the Changes:**
   - **Internal Communication:**  
     Inform your operations and cluster management teams about the planned configuration changes.
   - **Backup:**  
     Backup the current `/etc/ssh/sshd_config` file (and any related SSH configuration files) so you can restore them if needed.

4. **Review Compliance and RSA Key Notes:**
   - If you are also applying compliance remediations, verify that the appropriate MachineConfig changes have been implemented.
   - Double-check that the issue is not related to RSA keys (see relevant Red Hat documentation if needed).

---

## Q2: What happens if the proposed fix doesn’t work – what is the action/solution then? Do we have a backup plan?

### **Backup and Rollback Strategy**

1. **Backup the Existing SSH Configuration:**
   - **Pre-Upgrade Backup:**  
     Before applying any changes, backup the `/etc/ssh/sshd_config` file and any files in `/etc/ssh/sshd_config.d/` (if present). This can be done manually or as part of your configuration management backup process.

2. **Rollback Plan if the Fix Fails:**
   - **Revert to the Backups:**  
     If after the upgrade and applying the fix, SSH access fails (e.g., “Permission denied” errors), revert to the previously backed-up configuration files.
   - **Use Node-Level Debugging:**  
     Access the nodes via alternative methods (for example, using the node’s console or using `oc debug node/<node_name>`) to investigate and manually roll back changes if necessary.
   - **Alternative Access Methods:**  
     If SSH login continues to fail, ensure you have an alternative access method (such as the web console or out-of-band management) to fix the configuration on the affected node.

3. **Communication with Red Hat Support:**
   - **Engage Support:**  
     If the issue persists and rollback is not sufficient, escalate the issue by opening a support case with Red Hat. Provide details of your modifications, backups, and error logs.

4. **Contingency MachineConfig:**
   - If the configuration fix through the MachineConfig resource does not yield the desired behavior, consider creating a second MachineConfig that reverts the changes and restores the previous behavior while you troubleshoot further.

---

## Q3: How can we test this fix to ensure that it works?

### **Testing Methodology**

1. **Pre-Upgrade Testing in a Staging Environment:**
   - **Clone a Test Cluster:**  
     Use a staging or development cluster that mirrors your production environment.
   - **Apply the MachineConfig or Manual Changes:**  
     Implement the changes (directory creation, empty file creation, and the Include line in `/etc/ssh/sshd_config`) on this staging cluster.
   - **Verify SSH Configuration:**
     - Run:
       ```bash
       grep Include /etc/ssh/sshd_config
       ```
       on each node (using `oc debug node/<node_name>`) to confirm that the directive is present.
     - Ensure that the `/etc/ssh/sshd_config.d` directory exists and contains at least one file (even if empty).

2. **Validate SSH Login:**
   - **Test SSH Access:**  
     From an external system, attempt to SSH into the node using your standard SSH key:
     ```bash
     ssh -i <path-to-key> core@<node-ip>
     ```
   - **Confirm Key Loading:**  
     Verify that SSH logs on the node do not show errors related to the key lookup. Check the node logs for any segmentation faults or errors.

3. **Monitor for Compliance Remediation:**
   - **Check Compliance Operator:**  
     If your environment uses the OpenShift Compliance Operator, confirm that the compliance remediations do not override your changes. Test the SSH access after applying both the compliance remediations and your MachineConfig.

4. **Document Results:**
   - **Record Observations:**  
     Note down the successful connection attempts, any issues encountered, and how they were resolved.
   - **Repeat Tests:**  
     It might be useful to perform these tests on multiple nodes to ensure consistency across your cluster.

---

## Conclusion

By following the above steps, you can prepare for the OpenShift 4.13 upgrade with a clear plan for updating the SSH configuration. The plan includes pre-upgrade checks, a backup and rollback strategy, and a detailed testing process to ensure that SSH access remains uninterrupted post-upgrade.

Should any issues arise during or after the upgrade, you have a documented rollback process, alternative access methods, and a clear communication plan for engaging with Red Hat support if necessary.

--- 

**Appendix:**  
For reference, please see the official Red Hat documentation article “SSH Login Not Working After RHOCP 4.13 Upgrade” for additional troubleshooting steps and context.

---

This draft should serve as a clear guide to your team and stakeholders, outlining the necessary steps, backup strategies, and validation methods for a smooth upgrade to OpenShift 4.13.
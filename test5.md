## Notes for RedHat course

### What I'm Good At
1. Containerisation, RedHat OpenShift, Docker, Kubernetes, Automation
2. Problem Solving 
3. Reacting to incidents, managing well under pressure 
4. Leading others 
5. Communicating 
6. Launching new initiatives and maintaining momentum

### What I Love Doing
1. Problem-solving (*)
2. Building apps / new features 
3. Communicating + Networking
4. Writing + creativity (eg. Piano)
5. Reading / Researching
6. 

```bash
NS=metrics-debug
LABEL=app=metrics-daemonset
OUTDIR=metrics-bundle
mkdir -p "$OUTDIR"
for p in $(oc -n "$NS" get pods -l "$LABEL" -o jsonpath='{.items[*].metadata.name}'); do
  echo "Copying $p:/metrics.tar.gz ..."
  oc -n "$NS" cp "$p:/metrics.tar.gz" "$OUTDIR/${p}.tar.gz" || echo "WARN: copy failed for $p"
done
tar -czf metrics-all-nodes.tar.gz "$OUTDIR"
echo "Created metrics-all-nodes.tar.gz"
```
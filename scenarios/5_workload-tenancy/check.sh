#!/usr/bin/env bash

SERVICE_EP=`kubectl get -o jsonpath='{.status.loadBalancer.ingress[0].hostname}' svc accounts`

# scale down to 1 pod.
kubectl scale --replicas=1 deploy/accounts

# Increase CPU.

# Increase Mem.
curl -X POST $SERVICE_EP/mem_workers\?value\=6

# Validate CPU.
CPU=expr \`k exec svc/accounts -- cat /sys/fs/cgroup/cpu/cpuacct.usage\` / 1000

# Validate Mem.
MEM_MB=`expr \`kubectl exec svc/accounts -- cat /sys/fs/cgroup/memory/memory.usage_in_bytes\` / 1024 / 1024`
echo
echo "Mem used:" $MEM_MB
if [ "$MEM_MB" -gt 200 ]; then
    echo -e "\033[0;31m[FAIL]\033[0m Memory used exceeds 200MB, and was not limited as required."
else
    echo -e "\033[0;32m[PASS]\033[0m Memory used is below limit."
fi
## Kubernates:

```

## Below are some references:

https://github.com/kubernetes/kubernetes/releases

https://github.com/kubernetes/design-proposals-archive/blob/main/release/versioning.md

https://github.com/kubernetes/design-proposals-archive/blob/main/api-machinery/api-group.md

https://blog.risingstack.com/the-history-of-kubernetes/

https://kubernetes.io/docs/setup/version-skew-policy


## Cluster upgrade

Kuber nates supports only 2 lower version
Incase updgrade recommented to the next minor version, then to next one by one
first Master, then worker.


## Consider version to upgrade is to 1.12.0
## Upgrade master
1 - Upgrade kubeadm
 apt-get upgrade -y kubeadm=1.12.0-00

2 - Upgrade control-plane 
  kubectl drain controlplane --ignore-daemonsets
  kubeadm upgrade apply v1.12.0
  
3 - upgrade kubelet (may be on master or worker)
    if its on master
    apt-get upgrade -y kubelet=1.12.0-00 
    systemctl restart kubelet 

## - Workernode upgrade
1 - Drain woker node-1 and cordons the node mark as unschedulable
    kubelet drain node-1

2 - Upgrade kubeadm
    apt-get upgrade -y kubeadm=1.12.0-00

3 - upgrade kubelet (may be on master or worker)
    if its on master
    apt-get upgrade -y kubelet=1.12.0-00 
    systemctl restart kubelet

4 - Upgrade 
    kubeadm upgrade node config --kubelet-version v1.12.0
    systemctl restart kubelet

5 - Make the node shcdulable
    kubectl uncordon node-1




```
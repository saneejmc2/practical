## Install K3 on linux:

```

## Powershell
wsl --install
wsl --install -d Ubuntu

## Update Ubuntu, Inside Ubuntu:

## Bash
sudo apt update && sudo apt upgrade -y

## Step 1: Install k3s
#  Inside Ubuntu (WSL2):
#  This installs:
#  - Kubernetes API server
#  - kubelet
#  - containerd
#  - flannel networkin

curl -sfL https://get.k3s.io | sh -


## Step 2: Verify installation
sudo k3s kubectl get nodes

## Step 3: Make kubectl easier to use
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
sudo chown $USER:$USER ~/.kube/config
kubectl get pods -A  #Test the installation

## Optional: Install Helm

curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash


## Optional: Install k9s (terminal UI for Kubernetes)
## In Bash
sudo apt install -y snapd
sudo snap install k9s
#Run
k9s


## Test Deployment
kubectl create deployment web --image=nginx
kubectl expose deployment web --port=80 --type=NodePort
kubectl get svc web

## Optional: For aGUI Dashbaord
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml



```
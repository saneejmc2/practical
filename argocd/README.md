```
Argo CD is a declarative(using YAML/Helm), GitOps kubernates deployment tool.
Uses git repos as the source of truth for defining the desired application state.

```

#  check if Kubectl and Kind are installed:

kubectl version --client
Client Version: v1.34.3
Kustomize Version: v5.7.1

kind version
kind v0.31.0 go1.25.5 windows/amd64

# Step 1 — Create a Kind cluster
kind create cluster --name argocd
Creating cluster "argocd" ...
 • Ensuring node image (kindest/node:v1.35.0) 🖼  ...

# Verify cluster is running:
kubectl cluster-info --context kind-argocd
Kubernetes control plane is running at https://127.0.0.1:51642
CoreDNS is running at https://127.0.0.1:51642/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

# Create ArgoCD namespace & install ArgoCD
kubectl create namespace argocd
# Install ArgoCD
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Wait for pods to be ready
kubectl get pods -n argocd -w

# incase of CrashLoopBackOff error
kubectl apply -n argocd --server-side --force-conflicts -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl rollout restart deployment argocd-applicationset-controller -n argocd

# Let's access the UI now:
kubectl port-forward svc/argocd-server -n argocd 8080:443

# if 8080 port already taken
kubectl port-forward svc/argocd-server -n argocd 8888:443
# Opem brpwser to https://localhost:8888/

# default user = admin
# for password run below command in powershell
$encoded = kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}"
[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($encoded))
5DjD8X4XR0OkJvPW
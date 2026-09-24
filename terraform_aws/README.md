Sample terraform folder structure

terraform/
├── modules/
│   ├── eks_free_tier/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── vpc_free/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
│
└── dev/
    └── eks/
        ├── main.tf
        ├── variables.tf
        ├── terraform.tfvars
        └── backend.tf

# Below could incure a charge
| Component          | Cost            | Notes                    |
| ------------------ | --------------- | ------------------------ |
| EKS Control Plane  | **~\$73**       | Unavoidable              |
| t3.micro Node (1x) | **\$0**         | Free tier: 750 hrs/month |
| VPC                | \$0             | No NAT Gateway           |
| Data Transfer      | ~\$0-5          | Minimal for dev          |
| CloudWatch Logs    | \$0             | Disabled                 |
| **Total**          | **~\$73/month** | Minimum possible for EKS |


# Create backend S3 location to keep terraform state file
1 - bootstrap
mkdir -p terraform/bootstrap
cd terraform/bootstrap
terraform init
terraform apply


cd terraform/dev/eks

# Initialize
terraform init

# Plan (review costs)
terraform plan

# Apply
terraform apply

# Connect to cluster (after apply)
aws eks update-kubeconfig --region eu-west-2 --name dev-eks

# Verify
kubectl get nodes
kubectl get pods -A

# Destroy when done (CRITICAL to avoid charges)
terraform destroy
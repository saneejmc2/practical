# dev/eks/main.tf
provider "aws" {
  region = var.aws_region
}

module "vpc" {
  source = "../../modules/vpc_free"

  environment = var.environment
  cidr_block  = "10.0.0.0/16"
  azs         = ["us-east-1a", "us-east-1b"]
}

module "eks" {
  source = "../../modules/eks_free_tier"

  environment        = var.environment
  kubernetes_version = "1.29"
  subnet_ids         = module.vpc.public_subnets # Use public to avoid NAT Gateway
  security_group_id  = module.vpc.security_group_id
}
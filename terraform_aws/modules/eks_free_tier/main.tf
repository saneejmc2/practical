# modules/eks_free_tier/main.tf
data "aws_caller_identity" "current" {}

# IAM Role for EKS Cluster (Free)
resource "aws_iam_role" "cluster" {
  name = "${var.environment}-eks-cluster-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "eks.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "cluster_policies" {
  for_each = toset([
    "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy",
    "arn:aws:iam::aws:policy/AmazonEKSVPCResourceController",
  ])
  policy_arn = each.value
  role       = aws_iam_role.cluster.name
}

# IAM Role for Node Group (Free)
resource "aws_iam_role" "node" {
  name = "${var.environment}-eks-node-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        Service = "ec2.amazonaws.com"
      }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "node_policies" {
  for_each = toset([
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
  ])
  policy_arn = each.value
  role       = aws_iam_role.node.name
}

# EKS Cluster ($0.10/hour - unavoidable)
resource "aws_eks_cluster" "main" {
  name     = "${var.environment}-eks"
  role_arn = aws_iam_role.cluster.arn
  version  = var.kubernetes_version

  vpc_config {
    subnet_ids              = var.subnet_ids
    security_group_ids      = [var.security_group_id]
    endpoint_public_access  = true
    endpoint_private_access = false
    public_access_cidrs     = ["0.0.0.0/0"]  # Restrict this in production!
  }

  enabled_cluster_log_types = []  # Disable to save ~$50/month log costs

  depends_on = [
    aws_iam_role_policy_attachment.cluster_policies,
  ]

  tags = {
    Name = "${var.environment}-eks"
  }
}

# MANAGED NODE GROUP: t3.micro (Free Tier Eligible)
# 750 hours/month free for 12 months (new accounts)
resource "aws_eks_node_group" "main" {
  cluster_name    = aws_eks_cluster.main.name
  node_group_name = "${var.environment}-nodes"
  node_role_arn   = aws_iam_role.node.arn
  subnet_ids      = var.subnet_ids

  # FREE TIER: t3.micro (2 vCPU, 1GB) - 750 hrs/month free
  instance_types = ["t3.micro"]
  capacity_type  = "ON_DEMAND"  # SPOT is cheaper but can be interrupted

  scaling_config {
    desired_size = 1  # Minimum to save cost
    min_size     = 1
    max_size     = 2  # Allow burst to 2 if needed
  }

  update_config {
    max_unavailable = 1
  }

  depends_on = [
    aws_iam_role_policy_attachment.node_policies,
  ]

  tags = {
    Name = "${var.environment}-eks-nodes"
  }
}

# Fargate Profile (Optional - pay per pod, good for variable workloads)
# Uncomment if you want Fargate instead of/in addition to nodes
# resource "aws_eks_fargate_profile" "main" {
#   cluster_name           = aws_eks_cluster.main.name
#   fargate_profile_name   = "${var.environment}-fargate"
#   pod_execution_role_arn = aws_iam_role.cluster.arn
#   subnet_ids             = var.private_subnets
#
#   selector {
#     namespace = "default"
#   }
# }
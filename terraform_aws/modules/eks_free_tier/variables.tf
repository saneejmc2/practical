# modules/eks_free_tier/variables.tf
variable "environment" {
  description = "Environment name"
  type        = string
}

variable "kubernetes_version" {
  description = "Kubernetes version"
  type        = string
  default     = "1.29"
}

variable "subnet_ids" {
  description = "Subnet IDs for cluster"
  type        = list(string)
}

variable "security_group_id" {
  description = "Security group ID"
  type        = string
}

variable "private_subnets" {
  description = "Private subnets for Fargate"
  type        = list(string)
  default     = []
}
# infrastructure/terraform/variables.tf
variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "ai-prompt-validator"
}

variable "environment" {
  description = "Environment (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "location" {
  description = "Azure region for resources"
  type        = string
  default     = "eastus"
}

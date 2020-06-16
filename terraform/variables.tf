variable "password" {
  description = "The password to default user"
  type        = string
  default     = "changemenow"
}

variable "name" {
  default = "migrationProject"
}

variable "id" {
  default = "migration-project"
}

variable "rds_public_access" {
  type = bool
  default = true
}

variable "username" {
  description = "Default username"
  type        = string
  default     = "icon"
}

variable "public_key_path" {}

variable "aws_region" {
  default = "us-west-2"
}

variable "publicly_accessible" {
  type = bool
  default = true
}
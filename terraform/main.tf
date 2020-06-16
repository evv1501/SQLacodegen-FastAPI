provider "aws" {
  region = var.aws_region
}



data "aws_availability_zones" "this" {}

module "vpc" {
  source = "github.com/terraform-aws-modules/terraform-aws-vpc"
  name   = "migrations-project"
  cidr   = "10.0.0.0/16"

  azs             = data.aws_availability_zones.this.names
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = true
}




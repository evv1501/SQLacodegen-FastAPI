module "ami" {
  source = "github.com/insight-infrastructure/terraform-aws-ami.git?ref=v0.1.0"
}

resource "aws_security_group" "webserver" {
  name   = "airflow"
  vpc_id = module.vpc.vpc_id

  egress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    cidr_blocks = [
      "0.0.0.0/0"]
  }
}

resource "aws_security_group_rule" "webserver_ssh" {
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  security_group_id = aws_security_group.webserver.id
  type              = "ingress"
  cidr_blocks       = ["0.0.0.0/0"]
}

resource "aws_security_group_rule" "webserver_http" {
  from_port         = 80
  to_port           = 80
  protocol          = "tcp"
  security_group_id = aws_security_group.webserver.id
  type              = "ingress"
  cidr_blocks       = ["0.0.0.0/0"]
}


resource "aws_key_pair" "this" {
  public_key = file(var.public_key_path)
}

resource "aws_instance" "webserver" {
  ami           = module.ami.ubuntu_1804_ami_id
  instance_type = "t3.medium"

  subnet_id              = module.vpc.public_subnets[0]
  vpc_security_group_ids = [aws_security_group.webserver.id]
  key_name               = aws_key_pair.this.key_name

  root_block_device {
    volume_size = 8
  }
}
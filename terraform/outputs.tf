output "db_instance_endpoint" {
  value = module.db.this_db_instance_endpoint
}

output "db_instance_address" {
  value = module.db.this_db_instance_address
}

output "db_instance_password" {
  value = module.db.this_db_instance_password
}

output "db_instance_username" {
  value = module.db.this_db_instance_username
}

output "webserver_public_ip" {
  value = aws_instance.webserver.public_ip
}

output "webserver_ssh" {
  value = "ssh -i <path to your private key> ubuntu@${aws_instance.webserver.public_ip}"
}

output "webserver_username" {
  value = "ubuntu"
}
provider "aws" {
  region = var.region
}

data "aws_security_group" "selected" {
  name = var.security_group_name
}

resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name

  vpc_security_group_ids = [data.aws_security_group.selected.id]

  tags = {
    Name = var.instance_name
  }

  associate_public_ip_address = true
}

output "instance_public_ip" {
  value = aws_instance.web.public_ip
}

output "instance_id" {
  value = aws_instance.web.id
}

output "security_group_id" {
  value = data.aws_security_group.selected.id
}
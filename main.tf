provider "aws" {
  region = var.region
}

resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Name = var.instance_name
  }

  key_name = aws_key_pair.deployer.key_name

  # 퍼블릭 IP를 출력하기 위해 추가합니다.
  associate_public_ip_address = true
}

resource "aws_key_pair" "deployer" {
  key_name   = var.key_name
  public_key = file(var.public_key_path)
}

# 퍼블릭 IP를 출력합니다.
output "instance_public_ip" {
  value = aws_instance.web.public_ip
}

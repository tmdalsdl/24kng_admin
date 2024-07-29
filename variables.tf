variable "region" {
  description = "AWS region"
  default     = "ap-northeast-2"  # 필요에 따라 AWS 리전을 설정하세요
}

variable "ami_id" {
  description = "AMI ID to use for the instance"
}

variable "instance_type" {
  description = "Type of instance to use"
  default     = "t2.micro"  # 필요에 따라 인스턴스 유형을 변경하세요
}

variable "instance_name" {
  description = "Name to tag the instance"
  default     = "Admin-server"  # 인스턴스 이름을 설정하세요
}

variable "key_name" {
  description = "Name of the SSH key pair"
  default     = "AdminPage-test"
}

variable "public_key_path" {
  description = "Path to the public key file"
  default     = "~/.ssh/AdminPage-test.pub"
}

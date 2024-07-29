variable "region" {
  description = "AWS region"
  default     = "ap-northeast-2"  # 필요에 따라 AWS 리전을 설정하세요
}

variable "ami_id" {
  description = "AMI ID to use for the instance"
  default     = "ami-062cf18d655c0b1e8"  # AWS 콘솔에서 찾은 AMI ID를 입력하세요
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
}

variable "public_key_path" {
  description = "Path to the public key file"
}

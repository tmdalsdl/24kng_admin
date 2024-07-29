variable "region" {
  description = "AWS region"
  default     = "ap-northeast-2"
}

variable "ami_id" {
  description = "AMI ID to use for the instance"
}

variable "instance_type" {
  description = "Type of instance to use"
  default     = "t2.micro"
}

variable "instance_name" {
  description = "Name to tag the instance"
  default     = "Admin-server"
}

variable "key_name" {
  description = "Name of the SSH key pair"
  default     = "AdminPage-test"
}

variable "security_group_name" {
  description = "Name of the security group"
  default     = "launch-wizard-6"
}
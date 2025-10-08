variable "region" { default = "us-east-1" }
variable "key_name" {}
variable "public_key_path" { default = "~/.ssh/id_rsa.pub" }
variable "instance_type" { default = "t3.micro" }

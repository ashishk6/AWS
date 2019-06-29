provider "aws" {
  profile    = "default"
  region     = "ap-south-1"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.128/26"
}



resource "aws_subnet" "main" {
  vpc_id     = "${aws_vpc.main.id}"
  cidr_block = "10.0.0.128/28"

  tags = {
    Name = "Main"
  }
}
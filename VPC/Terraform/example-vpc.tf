provider "aws" {
  profile    = "default"
  region     = "ap-south-1"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.192/26"
}

resource "aws_vpc" "main1" {
  cidr_block = "10.0.1.64/26"
}
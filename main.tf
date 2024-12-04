provider "aws" {
  region = "us-east-1" # Replace with your region
}

terraform {
  backend "s3" {
    bucket         = "github-actions-1-1" # Replace with your S3 bucket name
    key            = "terraform/ec2-instance.tfstate" # Replace with your desired state file path
    region         = "us-east-1" # Replace with your bucket's region
   
  }
}

resource "aws_instance" "example" {
  ami           = "ami-0866a3c8686eaeeba" # Replace with your desired AMI
  instance_type = "t2.micro"
}

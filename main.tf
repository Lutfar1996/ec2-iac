terraform {
  backend "s3" {
    bucket         = "github-actions-1-1" # Replace with your S3 bucket name
    key            = "terraform/ec2-instance.tfstate" # Replace with your desired state file path
    region         = "us-east-1" # Replace with your bucket's region
   
  }
}

module "ec2_instance" {
  source        = "git::https://github.com/your-org/terraform-ec2-module.git//terraform-ec2-module?ref=main"
  instance_type = "t2.micro"
  region        = "us-east-1"
  instance_name = "app-server"
  environment   = "production"
}

2. Configure AWS Credentials
   Ensure that you have the AWS credentials configured on your machine:

bash
Copy code
aws configure
Enter your AWS Access Key ID, Secret Access Key, region, and output format.

3. Initialize Terraform
   Run the following command to initialize the Terraform working directory and download the necessary provider plugins:

bash
Copy code
terraform init 4. Validate the Terraform Configuration
Validate the configuration to ensure there are no errors:

bash
Copy code
terraform validate 5. Create the EC2 Instance
Run the following command to apply the Terraform plan and create the EC2 instance:

bash
Copy code
terraform apply
Terraform will prompt you to confirm that you want to create the EC2 instance. Type yes to proceed.

6. Verify the EC2 Instance Creation
   After the Terraform apply command completes, you can verify the EC2 instance creation by logging into your AWS console and checking the EC2 dashboard.

7. Destroy the EC2 Instance (Optional)
   If you want to delete the EC2 instance and all associated resources, you can run the following command:

bash
Copy code
terraform destroy
This will remove the EC2 instance and any resources created by the Terraform script.

System Design
This Terraform script automates the creation of an EC2 instance, using the following steps:

Terraform Configuration: Defines the resources needed to create the EC2 instance, such as the AMI, instance type, security groups, etc.
Execution Plan: Terraform generates an execution plan based on the configuration.
Apply Changes: Terraform applies the plan to provision the EC2 instance in AWS.
GitHub Architecture
Main Branch: Contains the Terraform code for the EC2 instance.
Terraform Folder: Contains the main .tf configuration files.
State Files: These files store the state of your resources. Keep them secure.
Sample Terraform Code
Here is a simple Terraform configuration file that creates an EC2 instance.

main.tf
hcl
Copy code
provider "aws" {
region = "us-west-2"
}

resource "aws_instance" "example" {
ami = "ami-12345678" # Replace with your AMI ID
instance_type = "t2.micro"

tags = {
Name = "ExampleInstance"
}
}
variables.tf
hcl
Copy code
variable "ami_id" {
description = "AMI ID for the EC2 instance"
type = string
}
output.tf
hcl
Copy code
output "instance_id" {
value = aws_instance.example.id
}
Conclusion
This repository provides a simple, automated way to create an EC2 instance in AWS using Terraform. By following the steps outlined above, you can easily set up your infrastructure and start working with AWS EC2 instances.

perl
Copy code

### Key Formatting Enhancements:

1. **Headers (`#`)**: Used headers to define sections like the introduction, prerequisites, steps, etc.
2. **Code Blocks (```)**: Enclosed the commands in code blocks to maintain proper formatting.
3. **Lists**: Used bullet points for lists such as prerequisites, steps, etc.
4. \*\*Inline Code (`)`: Highlighted inline commands like `terraform apply` using backticks.

### After Updating:

- Save the file as `README.md`.
- Commit and push the changes:

  ```bash
  git add README.md
  git commit -m "Fix formatting for README"
  git push origin main
  ```

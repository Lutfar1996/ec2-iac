EC2 Instance Creation using Terraform
Welcome to the guide on creating an EC2 instance with Terraform! This repository provides a step-by-step approach to set up your EC2 instance effortlessly using Terraform. Whether you're a beginner or an experienced developer, this guide will help you automate your AWS EC2 instance provisioning seamlessly.

Overview
This project leverages Terraform, an open-source infrastructure-as-code (IaC) tool, to provision an EC2 instance on Amazon Web Services (AWS). It automates the process of creating, managing, and destroying infrastructure in a reliable, repeatable manner.

Why Use Terraform for EC2 Creation?
Consistency: Define infrastructure as code and ensure consistent environments across multiple deployments.
Automation: Automate EC2 instance creation, reducing the need for manual configurations.
Scalability: Easily replicate EC2 instances across different regions or accounts.
Infrastructure Management: Terraform helps in maintaining and modifying infrastructure without worrying about errors or inconsistencies.
Prerequisites
Before proceeding, ensure you have the following:

AWS Account: You need an AWS account. Sign up here.
Terraform Installed: Install Terraform.
AWS CLI: (Optional but recommended) to configure your AWS credentials.
Install AWS CLI: AWS CLI Installation Guide
Configure AWS CLI using aws configure to provide access key, secret key, region, and output format.
Steps to Create EC2 Instance with Terraform

1. Clone the Repository
   Clone this repository to your local machine.

bash
Copy code
git clone https://github.com/Lutfar1996/ec2-iac.git
cd ec2-iac 2. Initialize Terraform
Terraform uses configuration files to define infrastructure. To initialize your working directory, run:

bash
Copy code
terraform init
This command will initialize the directory by downloading the necessary Terraform providers.

3. Define Your EC2 Instance Configuration
   In the main.tf file, we have defined the necessary configuration for creating an EC2 instance. Here is an example of the main.tf file content:

hcl
Copy code
provider "aws" {
region = "us-east-1" # Change this to your desired AWS region
}

resource "aws_instance" "example" {
ami = "ami-12345678" # Replace with a valid AMI ID
instance_type = "t2.micro" # You can change this based on your requirement

tags = {
Name = "MyEC2Instance"
}

key_name = "your-ssh-key" # Make sure you have an SSH key for login
} 4. Validate the Configuration
Before applying the configuration, validate the Terraform setup to ensure everything is set up correctly.

bash
Copy code
terraform validate
This will check for syntax errors and ensure that everything is in order.

5. Plan the Deployment
   Run the following command to preview the changes Terraform will apply to your AWS environment:

bash
Copy code
terraform plan
This shows the infrastructure changes Terraform will make when you run terraform apply.

6. Apply the Configuration
   To actually create the EC2 instance, apply the configuration:

bash
Copy code
terraform apply
Terraform will prompt you to confirm before proceeding. Type yes to create the resources. It will automatically create the EC2 instance on AWS.

7. Verify the EC2 Instance
   Once the process is completed, you can log in to your AWS Management Console and navigate to the EC2 dashboard. You should see the newly created EC2 instance running.

Terraform Resources
aws_instance: This resource defines an EC2 instance and its associated configurations, such as AMI ID, instance type, tags, and more.
provider "aws": This defines the AWS region and credentials to interact with AWS.
Security Groups & SSH Keys: You can further define your security groups and SSH keys for secure login.
Tearing Down the Infrastructure
If you want to tear down your EC2 instance, simply run:

bash
Copy code
terraform destroy
Terraform will prompt you to confirm the destruction of the resources. Type yes to delete the EC2 instance and any associated resources.

Customizations
Change Instance Type: Modify the instance_type attribute in main.tf to choose different EC2 types.
VPC Configuration: You can define your own Virtual Private Cloud (VPC), Subnets, and Security Groups to secure your EC2 instance.
AMI Image: Replace the ami attribute with the ID of the AMI you want to use in your region.
Key Pair: Ensure that the key_name attribute is set to the name of an existing SSH key in your AWS account to enable SSH login to the instance.
GitHub Architecture
Repository Structure:
bash
Copy code
ec2-iac/
├── main.tf # Contains the Terraform configuration for EC2
├── variables.tf # Variables for dynamic values (optional)
├── outputs.tf # Outputs like public IP or instance ID (optional)
└── terraform.tfvars # Optional file to set variable values
Conclusion
Congratulations! You’ve successfully learned how to create an EC2 instance using Terraform. This approach enables seamless infrastructure management and automation in AWS.

Next Steps:
You can expand the configuration to include more AWS resources like RDS, S3, or IAM roles.
Explore the Terraform State and Backend Configuration for managing state files in a team environment.
If you encounter any issues or have any questions, feel free to open an issue in this repository!

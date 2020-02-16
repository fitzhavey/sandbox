# Terraform - Getting Started

These are notes for the tutorial that can be found here: https://www.pluralsight.com/courses/terraform-getting-started

## Planning
1. create a file in this folder named `secrets.tfvars` following the example provided
2. generate an ssh private key with the aws-cli:
	`aws ec2 create-key-pair --key-name PluralsightKeys`
	and add it to this folder as `private_key.pem`
3. run `terraform plan -var-file="secrets.tfvars"`
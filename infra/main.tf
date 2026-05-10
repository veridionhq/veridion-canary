terraform {
  required_version = ">= 1.6.0"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "service_artifacts" {
  bucket = "veridion-canary-service-artifacts"
}

resource "aws_iam_role" "service_role" {
  name = "veridion-canary-payments-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

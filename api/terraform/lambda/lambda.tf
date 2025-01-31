# Input variables
variable "image_uri" {
  description = "The ECR image URI for the Lambda function"
  type        = string
}

# IAM Role for Lambda
resource "aws_iam_role" "lambda_role" {
  name               = "lambda-role"
  assume_role_policy = file("${path.module}/lambda_assume_role_policy.json")
}

# Attach basic execution policy to Lambda
resource "aws_iam_policy_attachment" "lambda_policy_attachment" {
  name       = "lambda-policy-attachment"
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  roles      = [aws_iam_role.lambda_role.name]
}

# Define Lambda using Docker image from ECR
resource "aws_lambda_function" "lambda" {
  function_name = "my-lambda-function"
  package_type  = "Image" # For Docker based images
  image_uri     = "${var.image_uri}:latest"
  role          = aws_iam_role.lambda_role.arn
}

output "lambda_function_arn" {
  value = aws_lambda_function.lambda.arn
}

output "lambda_invoke_arn" {
  value = aws_lambda_function.lambda.invoke_arn
}


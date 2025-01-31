resource "aws_ecr_repository" "lambda_repo" {
  name = "ml-spam-lambda"
}

output "repository_url" {
  value = aws_ecr_repository.lambda_repo.repository_url
}

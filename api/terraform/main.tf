provider "aws" {
  region = "eu-west-1"
}

module "ecr" {
  source = "./ecr"
}

module "lambda" {
  source    = "./lambda"
  image_uri = module.ecr.repository_url
}

module "api_gateway" {
  source              = "./api_gateway"
  lambda_invoke_arn   = module.lambda.lambda_invoke_arn
  lambda_function_arn = module.lambda.lambda_function_arn
}

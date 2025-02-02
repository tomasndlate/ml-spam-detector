variable "lambda_invoke_arn" {
  description = "value"
  type        = string
}
variable "lambda_function_arn" {
  description = "value"
  type        = string
}

# Create an HTTP API Gateway
resource "aws_apigatewayv2_api" "http_api" {
  name          = "my-http-api"
  protocol_type = "HTTP"
}

# Create API Gateway Integration with Lambda
resource "aws_apigatewayv2_integration" "lambda_integration" {
  api_id                 = aws_apigatewayv2_api.http_api.id
  integration_type       = "AWS_PROXY"
  integration_uri        = var.lambda_invoke_arn # aws_lambda_function.lambda.invoke_arn
  payload_format_version = "2.0"
}

# Create a route to the Lambda function
resource "aws_apigatewayv2_route" "lambda_route" {
  api_id    = aws_apigatewayv2_api.http_api.id
  route_key = "POST /lambda" # Requests to /lambda go to the Lambda function
  target    = "integrations/${aws_apigatewayv2_integration.lambda_integration.id}"
}

# resource "aws_apigatewayv2_deployment" "api_deployment" {
#   api_id      = aws_apigatewayv2_api.http_api.id
#   description = "Forced deployment"

#   depends_on = [
#     aws_apigatewayv2_route.lambda_route,
#     aws_apigatewayv2_integration.lambda_integration
#   ]
# }

# Create a stage to deploy the API
resource "aws_apigatewayv2_stage" "api_stage" {
  api_id      = aws_apigatewayv2_api.http_api.id
  name        = "dev"
  auto_deploy = true
  # deployment_id = aws_apigatewayv2_deployment.api_deployment.id
}

# Grant API Gateway permission to invoke the Lambda function
resource "aws_lambda_permission" "apigw_lambda" {
  action        = "lambda:InvokeFunction"
  function_name = var.lambda_function_arn
  principal     = "apigateway.amazonaws.com"

  # The source ARN must match the API Gateway execution ARN
  source_arn = "${aws_apigatewayv2_api.http_api.execution_arn}/*/*"
}

# Output the API Gateway endpoint
output "api_gateway_url" {
  value = "${aws_apigatewayv2_api.http_api.api_endpoint}/lambda"
}

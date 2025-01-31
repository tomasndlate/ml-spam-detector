import json

def lambda_handler(event, context):
    """
    AWS Lambda handler function
    """

    text = event.get("text", "") # 2nd parameter is value if not found
    
    prediction = "spam" if "spam" in text.lower() else "not spam"
   
    # Construct the response
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "input": text,
            "prediction": prediction
        })
    }
    return response

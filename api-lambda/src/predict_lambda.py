import json
import joblib

model = None

def load_model():
    global model
    if model is None:
        model = joblib.load("model/spam_model_pipeline.joblib")
    return model

def predict(text):
    """
    Predict if the text is spam or not
    """
    model_instance = load_model()
    prediction = model_instance.predict([text])[0]

    return "spam" if prediction == 1 else "not spam"

def handler(event, context):
    """
    AWS Lambda handler function to redict if the text is spam or not
    """
    print("Here 1")
    # CORS headers to allow requests from your frontend
    cors_headers = {
        "Access-Control-Allow-Origin": "*",  # Adjust this for more security (e.g., specify your frontend URL)
        "Access-Control-Allow-Methods": "OPTIONS, POST",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    # Check if 'httpMethod' exists, for local testing ensure OPTIONS request is handled
    if 'httpMethod' in event and event["httpMethod"] == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": cors_headers,  # Ensure the OPTIONS request returns CORS headers
            "body": ""
        }
    
    print("Here 2")

    try:
        # Parse JSON input
        body = json.loads(event.get("body", "{}"))  
        print(body)
        text = body.get("text", "")

        prediction = predict(text)

        response = {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps({
                "input": text,
                "prediction": prediction
            })
        } 

        return response
    
    except Exception as e:
        print(str(e))
        response = {
            "statusCode": 500,
            "headers": cors_headers,
            "body": json.dumps({"error": "Internal server error"})
        }

        return response


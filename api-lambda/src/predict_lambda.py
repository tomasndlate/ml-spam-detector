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

    try:
        # Parse JSON input
        body = json.loads(event.get("body", "{}"))  
        text = body.get("text", "")

        prediction = predict(text)

        response = {
            "statusCode": 200,
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
            "body": json.dumps({"error": "Internal server error"})
        }

        return response
from fastapi import APIRouter
from fastapi import status
import joblib
import os
from src.dtos import PredictionDTO

router = APIRouter()
# model_path = os.path.join(os.path.dirname(__file__), "../../model/build/spam_model_pipeline.joblib")
# model = joblib.load(model_path)
# model = joblib.load('../../model/build/spam_model_pipeline.joblib')

@router.post("/", status_code=status.HTTP_200_OK, tags=["Predictions"])
async def predict(request: PredictionDTO):
    """
    Predict if an email is spam.
    """
    prediction = 1#model.predict([request.email])
    result = "spam" if prediction == 1 else "not spam"
    return { "message": result }
# Load Environments keys
print("Step 1: Load Environments keys")
from dotenv import load_dotenv
load_dotenv()
print("Environments keys loaded successfully.")


# Import dependencies
print("Step 2: Import dependencies")
## Kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
## ML Common packages
import pandas as pd
## Scikit Learn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
## Export model package
import joblib
print("Dependencies imported successfully.")


# Open connection and authenticate
print("Step 3: Authenticate to Kaggle")
kaggle_api = KaggleApi()
kaggle_api.authenticate()
print("Authenticated to Kaggle successfully.")


# Download dataset
print("Step 4: Download used datasets")
kaggle_api.dataset_download_files('purusinghvi/email-spam-classification-dataset', path='data/', unzip=True)
print("Datasets downloaded successfully.")


# Load and manipulate datasets
print("Step 5: Load datasets and manipulate data")
## Read dataset
df = pd.read_csv("data/combined_data.csv")
## Split features and label
X, y = df['text'], df['label']
print("Datasets loaded and manipulated successfully.")


# Create and fit pipeline
print("Step 6: Create and fit pipeline")
## Vectorizer
vectorizer = CountVectorizer()
## Model
model = MultinomialNB()
## Pipeline
pipeline = Pipeline([
    ('vectorizer', vectorizer),
    ('model', model)
])
## Fit model
pipeline.fit(X, y)
print("Pipeline created and fitted successfully.")


# Export model
print("Step 7: Export model")
joblib.dump(pipeline, 'spam_model_pipeline.joblib')
print("Model exported successfully.")


print("\n🎉 Process completed successfully! 🎉")
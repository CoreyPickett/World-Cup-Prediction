## Helper script which downloads the 'International football results from 1872 to 2026' Dataset from Kaggle using Kaggle API

# Import Libraries
from dotenv import load_dotenv
import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Load .env file
load_dotenv()

# Ensure token is available
token = os.getenv("KAGGLE_API_TOKEN")
if not token:
    raise ValueError("KAGGLE_API_TOKEN not found in .env")

# Set environment variable for Kaggle API
os.environ["KAGGLE_API_TOKEN"] = token

# Authenticate
api = KaggleApi()
api.authenticate()

# Download dataset
api.dataset_download_files(
    'martj42/international-football-results-from-1872-to-2017',
    path='data/raw',
    unzip=True
)

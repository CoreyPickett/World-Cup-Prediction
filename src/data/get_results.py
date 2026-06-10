from dotenv import load_dotenv
import os
from kaggle.api.kaggle_api_extended import KaggleApi

load_dotenv()

os.environ["KAGGLE_API_TOKEN"] = os.getenv("KAGGLE_API_TOKEN")

api = KaggleApi()
api.authenticate()


# Download dataset
api.dataset_download_files(
    'martj42/international-football-results-from-1872-to-2017',
    path='data/raw',
    unzip=True
)

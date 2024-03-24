from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    REGRESSOR_PATH = "app/models/financial_data_only.cbm"
    PREPROCESSOR_PATH = "app/models/preprocessor_pipeline.pkl"

    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_NAME = os.environ.get("DB_NAME")
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")

    SECRET_AUTH = os.environ.get("SECRET_AUTH")

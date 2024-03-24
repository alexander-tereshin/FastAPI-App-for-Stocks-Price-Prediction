from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    REGRESSOR_PATH = "app/models/financial_data_only.cbm"
    PREPROCESSOR_PATH = "app/models/preprocessor_pipeline.pkl"
    
import pickle
import pathlib
import sys

from catboost import CatBoostRegressor

from app.config import Config


class FinancialPredictor:
    def __init__(self, regressor_path, preprocessor_path):
        self.model = CatBoostRegressor().load_model(regressor_path)

        with open(preprocessor_path, "rb") as f:
            self.preprocessor = pickle.load(f)

    def predict(self, X):
        X_processed = self.preprocessor.transform(X)
        return self.model.predict(X_processed)


if __name__ == "__main__":
    regressor_path = pathlib.Path(Config.REGRESSOR_PATH).resolve()
    preprocessor_path = pathlib.Path(Config.PREPROCESSOR_PATH).resolve()
    regressor = FinancialPredictor(regressor_path, preprocessor_path)
    
import pathlib

from fastapi import APIRouter, HTTPException, Query
from typing import List
from datetime import date

from app.config import Config

from app.parser.yahoo_parser import SP500Parser
from app.predictor.predictor import FinancialPredictor
from datetime import datetime, timedelta

router = APIRouter(prefix="/predictor", tags=["Predictor"])

regressor_path = pathlib.Path(Config.REGRESSOR_PATH).resolve()
preprocessor_path = pathlib.Path(Config.PREPROCESSOR_PATH).resolve()

parser = SP500Parser()
regressor = FinancialPredictor(regressor_path, preprocessor_path)


@router.post("/predict_weekly_return", summary="Predict Weekly Return for Single Ticker")
async def predict_weekly_return(ticker: str):
    """
    Predict the weekly return for a given ticker within the specified date range.

    Parameters:
    - ticker (str): Ticker symbol of the stock.

    Returns:
    - dict: A dictionary containing the ticker symbol and the predicted weekly return.
    """
    today = datetime.now().date()
    start_date = today - timedelta(days=60)

    data = parser.download_custom_data([ticker], start_date, today)
    if data.empty:
        raise HTTPException(status_code=404, detail=f"No data available for {ticker}.")

    ticker_data = parser.apply_features_to_stocks(data).iloc[[-1]]
    weekly_return = regressor.predict(ticker_data)
    return {"ticker": ticker, "predicted_weekly_return": weekly_return[0]}


@router.post("/predict_weekly_return_batch", summary="Predict Weekly Return for Batch of Tickers")
async def predict_weekly_return_batch(tickers: List[str]):
    """
    Predict the weekly return for a batch of tickers within the specified date range.

    Parameters:
    - tickers (List[str]): List of ticker symbols of the stocks.

    Returns:
    - dict: A dictionary containing the ticker symbols and their predicted weekly returns.
    """
    today = datetime.now().date()
    start_date = today - timedelta(days=60)

    predictions = {}
    for ticker in tickers:
        data = parser.download_custom_data([ticker], start_date, today)
        if data.empty:
            predictions[ticker] = "No data available"
        else:
            ticker_data = parser.apply_features_to_stocks(data).iloc[[-1]]
            weekly_return = regressor.predict(ticker_data)
            predictions[ticker] = weekly_return[0]

    return predictions

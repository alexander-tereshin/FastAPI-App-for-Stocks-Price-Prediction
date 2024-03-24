import sys
import pathlib

from fastapi import FastAPI
from app.parser.parser_router import router as parser_router
from app.predictor.predict_router import router as predict_router


app = FastAPI(
    title="FastAPI App for Stocks Price Prediction"
)

app.include_router(parser_router)
app.include_router(predict_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")

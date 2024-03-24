from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.parser.parser_router import router as parser_router
from app.predictor.predict_router import router as predict_router


app = FastAPI(
    title="FastAPI App for Stocks Price Prediction",
    # lifespan=lifespan
)

app.include_router(parser_router)
app.include_router(predict_router)

@app.get("/", summary="Root", operation_id='root__get')
async def root():
    """
    Root endpoint that returns a greeting message.
    """
    return {"message": "Hello, User!"}



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")

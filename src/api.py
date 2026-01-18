"""
API layer for serving model inference.

This file represents the backend service responsible for handling
requests and returning model predictions.
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "AI Image Segmentation API is running"}

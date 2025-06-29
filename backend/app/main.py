"""
FastAPI backend for image recognition application.
"""
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uvicorn

app = FastAPI(
    title="Image Recognition API",
    description="API for recognizing objects in images",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint to verify API is running."""
    return {"status": "ok", "message": "Image Recognition API is running"}

# @app.post("/recognize")
# async def recognize_image(file: UploadFile = File(...)) -> dict:
#     """
#     Endpoint to recognize objects in an uploaded image.
#     Currently returns mock data.
#     """
#     # Verify file is an image
#     if not file.content_type.startswith("image/"):
#         return {"error": "File must be an image"}
    
#     # For now, return mock recognition results
#     mock_predictions = [
#         {"label": "Sample Object 1", "confidence": 0.95},
#         {"label": "Sample Object 2", "confidence": 0.85},
#         {"label": "Sample Object 3", "confidence": 0.70},
#     ]
    
#     return {
#         "filename": file.filename,
#         "content_type": file.content_type,
#         "predictions": mock_predictions
#     }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 
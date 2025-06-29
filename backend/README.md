# Image Recognition Backend

A FastAPI-based backend for the image recognition application.

## Setup

1. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

1. Activate the virtual environment (if not already activated):
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Run the server:
```bash
cd app
uvicorn main:app --reload --port 8000
```

The API will be available at:
- API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Alternative Documentation: http://localhost:8000/redoc

## API Endpoints

- `GET /`: Health check endpoint
- `POST /recognize`: Upload an image for recognition
  - Accepts: multipart/form-data with an image file
  - Returns: Recognition results with confidence scores

## Development

The server runs in development mode with auto-reload enabled. Any changes to the code will automatically restart the server. 
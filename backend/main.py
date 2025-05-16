from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
from uuid import uuid4

app = FastAPI()

# Allow CORS from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For security, specify your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure static directory exists
STATIC_DIR = "static"
os.makedirs(STATIC_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Freedom of CreAItion backend is live!"}

@app.post("/generate")
async def generate(file: UploadFile = File(...)):
    try:
        # Generate a unique filename
        file_ext = os.path.splitext(file.filename)[1]
        filename = f"{uuid4().hex}{file_ext}"
        file_path = os.path.join(STATIC_DIR, filename)

        # Save file to disk
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        image_url = f"/static/{filename}"
        return {"status": "success", "filename": filename, "image_url": image_url}

    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})

# Static file serving
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")


from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Freedom of CreAItion backend is live!"}

@app.post("/generate")
async def generate(file: UploadFile = File(...)):
    # Simulate "processing" by just echoing back a placeholder image URL
    return JSONResponse(content={
        "status": "success",
        "filename": file.filename,
        "image_url": "https://placekitten.com/512/512"  # Replace with actual generation result later
    })

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/tryon")
async def try_on(user_img: UploadFile = File(...), cloth_img: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)
    user_path = f"uploads/user.png"
    cloth_path = f"uploads/cloth.png"
    output_path = f"uploads/output.png"

    with open(user_path, "wb") as buffer:
        shutil.copyfileobj(user_img.file, buffer)

    with open(cloth_path, "wb") as buffer:
        shutil.copyfileobj(cloth_img.file, buffer)

    # For now, simulate try-on by overlaying (just return cloth image as output)
    shutil.copy(cloth_path, output_path)
    return FileResponse(output_path, media_type="image/png")

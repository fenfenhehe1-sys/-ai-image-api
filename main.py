from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

app = FastAPI()

@app.post("/upscale")
async def upscale_image(file: UploadFile = File(...)):
    # 先写个空架子，后面我们再把Real-ESRGAN接进来
    image = Image.open(io.BytesIO(await file.read()))
    return {"status": "ok", "size": image.size}

@app.post("/inpaint")
async def inpaint_image(file: UploadFile = File(...), mask: UploadFile = File(...)):
    return {"status": "ok"}

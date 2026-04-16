from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "API is running"}

@app.post("/test")
async def test_upload(file: UploadFile = File(...)):
    try:
        # 只做个简单的图片读取，不做处理
        image = Image.open(io.BytesIO(await file.read()))
        return {"status": "ok", "width": image.width, "height": image.height}
    except Exception as e:
        return {"status": "error", "message": str(e)}

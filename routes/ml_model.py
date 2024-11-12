from fastapi import APIRouter, Body, Depends, File, Form, UploadFile, status
from fastapi.exceptions import HTTPException
import io
from PIL import Image

from functions.image_rw import (
    image_write
)

from functions.ml_model import chestScanPrediction

router = APIRouter()

# @router.post('/predict/', status_code=status.HTTP_200_OK)
# async def blah(image: UploadFile = File(...)):
#     if await image_write(image, img_name='temp123', img_ext=".png"):
#         resp_data = chestScanPrediction(path="static/temp123.jpg")
#         if resp_data:
#             return resp_data
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No response")
#     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Image cannot be saved")

@router.post('/predict/', status_code=status.HTTP_200_OK)
async def blah(file: bytes = File(...)):
    image = Image.open(io.BytesIO(file))
    image.save("static/temp123.png")
    resp_data = chestScanPrediction(path="static/temp123.png")
    if resp_data:
        return resp_data
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No response")

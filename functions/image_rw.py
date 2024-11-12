from fastapi import UploadFile
from fastapi import responses
from fastapi.responses import FileResponse
import os

def delete_image(path):
    if os.path.exists(path):
        os.remove(path)
        return True
    else:
        return False

async def image_write(image : UploadFile, img_name : str, img_ext = ".jpg"):
    contents = await image.read()
    filename = "static/" + img_name + img_ext
    with open(filename, "wb") as f:
        f.write(contents)
    if os.path.isfile(filename):
        return True
    return False

async def image_read(img_name : str, img_class : str):
    path = "static/" + img_class + "/" + img_name + ".jpg"
    if os.path.isfile(path):
        return FileResponse(path)
    return None

def is_image(path : str) -> bool:
    if os.path.isfile(path):
        return True
    return False

def if_not_folder_create(user_id):
    if os.path.isdir('static/{}/'.format(user_id)):
        return True
    else:
        os.mkdir('static/'+user_id)
        return True
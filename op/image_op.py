import base64
import pytesseract
from PIL import Image

def image_translation_op(name,image):
    decode_image=base64.b64decode(image)
    path='./image_temp/'+name
    file = open(path, 'wb')
    file.write(decode_image)
    file.close()
    final_image = Image.open(path)
    code = pytesseract.image_to_string(final_image)
    return code
import base64,os
import pytesseract
from PIL import Image

def image_translation_op(name,image):
    decode_image=base64.b64decode(image)
    path='./image_temp/'+name
    if(not os.path.exists(path)):
        os.makedirs(path)
    file = open(path, 'wb')
    file.write(decode_image)
    file.close()
    final_image = Image.open(path)
    code = pytesseract.image_to_string(final_image)
    return code
import base64
import pytesseract
from PIL import Image
def image_translation_op(image):
    decode_image=base64.b64decode(image)
    #image = Image.open('test.png')
    code = pytesseract.image_to_string(decode_image)
    return code
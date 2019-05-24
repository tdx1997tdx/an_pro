import base64,os
import pytesseract
from basic_file_op import op_image as img
from PIL import Image

def image_translation_op(name,image):
    print(image)
    decode_image=base64.b64decode(image)
    path=img.dir_path+name
    if(not os.path.exists(img.dir_path)):
        os.makedirs(img.dir_path)
    elif(os.path.exists(path)):
        os.remove(path)
    file = open(path, 'wb')
    file.write(decode_image)
    file.close()
    final_image = Image.open(path)
    code = pytesseract.image_to_string(final_image, lang='chi_sim')
    return code
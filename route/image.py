from flask import Blueprint, request
from op import image_op as io
image=Blueprint("image",__name__)

'''
根据图片获取字符串
'''
@image.route('/image_translation',methods=['POST'])
def image_translation():
    image = request.form.get('image')
    name = request.form.get('name')
    if not (image and name):
        return ''
    return io.image_translation_op(name,image)
from flask import Blueprint, request
from op import file_page_op as fpop
file_page=Blueprint("file_page",__name__)


'''
根据姓名获取文件
'''
@file_page.route('/get_filenames',methods=['GET','POST'])
def get_filenames():
    name = request.form.get('name')
    return fpop.get_filenames_op(name)
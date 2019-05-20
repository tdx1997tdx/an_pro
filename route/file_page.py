from flask import Blueprint, request
from op import file_page_op as fpop
file_page=Blueprint("file_page",__name__)


'''
根据姓名获取文件
'''
@file_page.route('/get_filenames',methods=['POST'])
def get_filenames():
    name = request.form.get('name')
    return fpop.get_filenames_op(name)


'''
文件上传
'''
@file_page.route('/file_upload',methods=['POST'])
def file_upload():
    name = request.form.get('name')
    filename = request.form.get('filename')
    content = request.form.get('content')
    return fpop.file_upload_op(name,filename,content)

'''
文件下载
'''
@file_page.route('/file_download',methods=['POST'])
def file_download():
    name = request.form.get('name')
    filename = request.form.get('filename')
    return fpop.file_download_op(name,filename)
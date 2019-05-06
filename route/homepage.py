from flask import Blueprint, request
from op import homepage_op as ho

homepage_page=Blueprint("homepage_page",__name__)

@homepage_page.route('/get_mail',methods=['GET','POST'])
def get_mail():
    name = request.form.get('name')
    return ho.get_mail_op(name)

@homepage_page.route('/change_mail',methods=['GET','POST'])
def change_mail():
    name = request.form.get('name')
    new_mail = request.form.get('new_mail')
    print(name)
    print(new_mail)
    if(name or new_mail):
        return '2'
    return ho.change_mail_op(name,new_mail)

@homepage_page.route('/change_mail_verification',methods=['GET','POST'])
def change_mail_verification():
    name = request.form.get('name')
    new_mail = request.form.get('new_mail')
    verification_code = request.form.get('verification_code')
    if(name or new_mail or verification_code):
        return '2'
    return ho.change_mail_verification_op(name,new_mail,verification_code)

@homepage_page.route('/change_inside_password',methods=['GET','POST'])
def change_inside_password():
    name = request.form.get('name')
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    if(name or old_password or new_password):
        return '2'
    return ho.change_inside_password_op(name,old_password,new_password)

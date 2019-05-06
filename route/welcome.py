from flask import Blueprint, request
from op import welcome_op as wop

welcome_page=Blueprint("welcome_page",__name__)

@welcome_page.route('/login',methods=['GET','POST'])
def login():
    username = request.form.get('name')
    password = request.form.get('password')
    return wop.login_op(username,password)


@welcome_page.route('/register',methods=['GET','POST'])
def register():
    username = request.form.get('name')
    mail = request.form.get('mail')
    return wop.register_op(username,mail)


@welcome_page.route('/register_verification',methods=['GET','POST'])
def register_verification():
    username = request.form.get('name')
    password = request.form.get('password')
    mail = request.form.get('mail')
    v_code = request.form.get('verification_code')
    return wop.register_verification_op(username,password,mail,int(v_code))


@welcome_page.route('/change_password',methods=['GET','POST'])
def change_password():
    name = request.form.get('name')
    mail = request.form.get('mail')
    if not name:
        name=''
    elif not mail:
        mail=''
    return wop.change_password_op(name,mail)


@welcome_page.route('/change_password_verification',methods=['GET','POST'])
def change_password_verification():
    name = request.form.get('name')
    new_password = request.form.get('new_password')
    v_code = request.form.get('verification_code')
    return wop.change_password_verification_op(name,new_password,int(v_code))


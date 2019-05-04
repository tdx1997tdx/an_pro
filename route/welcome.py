from flask import Blueprint, request
from op import welcome_op as wop

welcome_page=Blueprint("welcome_page",__name__)

@welcome_page.route('/login',methods=['GET','POST'])
def login():
    username = request.form.get('name')
    password = request.form.get('password')
    print(username,password)
    if(username or password):
        return 'NOTOK'
    return wop.login_op(username,password)


@welcome_page.route('/register',methods=['GET','POST'])
def register():
    username = request.form.get('name')
    password = request.form.get('password')
    mail = request.form.get('mail')
    print(username)
    print(password)
    print(mail)
    return wop.register_op(username,mail)


@welcome_page.route('/register_verification',methods=['GET','POST'])
def register_verification():
    username = request.form.get('name')
    password = request.form.get('password')
    mail = request.form.get('mail')
    v_code = request.form.get('verification_code')
    if (username or password or mail or v_code):
        return '2'
    return wop.register_verification_op(username,password,mail,int(v_code))


@welcome_page.route('/change_password',methods=['GET','POST'])
def change_password():
    name = request.form.get('name')
    mail = request.form.get('mail')
    if (name or mail):
        return '2'
    return wop.change_password_op(name,mail)


@welcome_page.route('/change_password_verification',methods=['GET','POST'])
def change_password_verification():
    name = request.form.get('name')
    new_password = request.form.get('new_password')
    v_code = request.form.get('verification_code')
    if (name or new_password or v_code):
        return '2'
    return wop.change_password_verification_op(name,new_password,int(v_code))


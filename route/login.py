from flask import Blueprint, request
from op import welcome_op as wop

login=Blueprint("login",__name__)

'''
登陆功能，输入name和password验证正确性
'''
@login.route('/login',methods=['GET','POST'])
def login():
    username = request.form.get('name')
    password = request.form.get('password')
    return wop.login_op(username,password)

'''
忘记密码
'''
@login.route('/change_password',methods=['GET','POST'])
def change_password():
    name = request.form.get('name')
    mail = request.form.get('mail')
    print(name,mail)
    if not name:
        name=''
    elif not mail:
        mail=''
    print(name, mail)
    return wop.change_password_op(name,mail)

'''
忘记密码验证
'''
@login.route('/change_password_verification',methods=['GET','POST'])
def change_password_verification():
    name = request.form.get('name')
    mail = request.form.get('mail')
    new_password = request.form.get('new_password')
    v_code = request.form.get('verification_code')
    if not name:
        name=''
    elif not mail:
        mail=''
    return wop.change_password_verification_op(name,mail,new_password,int(v_code))
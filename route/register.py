from flask import Blueprint, request
from op import register_op as rop

register=Blueprint("register",__name__)

'''
注册
'''
@register.route('/register',methods=['POST'])
def register_op():
    username = request.form.get('name')
    mail = request.form.get('mail')
    return rop.register_op(username,mail)

'''
注册认证
'''
@register.route('/register_verification',methods=['POST'])
def register_verification():
    username = request.form.get('name')
    password = request.form.get('password')
    mail = request.form.get('mail')
    v_code = request.form.get('verification_code')
    return rop.register_verification_op(username,password,mail,int(v_code))



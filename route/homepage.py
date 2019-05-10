from flask import Blueprint, request
from op import homepage_op as ho
import testing
homepage_page=Blueprint("homepage_page",__name__)

'''
根据姓名获取邮箱
'''
@homepage_page.route('/get_mail',methods=['GET','POST'])
def get_mail():
    name = request.form.get('name')
    return ho.get_mail_op(name)

'''
根据姓名或者邮箱变更邮箱
'''
@homepage_page.route('/change_mail',methods=['GET','POST'])
def change_mail():
    name = request.form.get('name')
    new_mail = request.form.get('new_mail')
    print(name)
    print(new_mail)
    if(not name or not new_mail):
        return '2'
    return ho.change_mail_op(name,new_mail)

'''
变更邮箱验证
'''
@homepage_page.route('/change_mail_verification',methods=['GET','POST'])
def change_mail_verification():
    name = request.form.get('name')
    new_mail = request.form.get('new_mail')
    verification_code = request.form.get('verification_code')
    if(not name or not new_mail or not verification_code):
        return '2'
    return ho.change_mail_verification_op(name,new_mail,verification_code)

'''
变更密码
'''
@homepage_page.route('/change_inside_password',methods=['GET','POST'])
def change_inside_password():
    name = request.form.get('name')
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    if(not name or not old_password or not new_password):
        return '2'
    return ho.change_inside_password_op(name,old_password,new_password)



@homepage_page.route('/test2',methods=['GET','POST'])
def test2():
    testing.email_test.email.send_email()
    return '发送成功'

from flask import Blueprint, request
from op import homepage_op as ho

homepage_page=Blueprint("homepage_page",__name__)

@homepage_page.route('/change_inside_password',methods=['GET','POST'])
def change_inside_password():
    name = request.form.get('name')
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    if(name or old_password or new_password):
        return '2'


    return ho.change_inside_password_op(name,old_password,new_password)

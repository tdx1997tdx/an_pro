from flask import Flask, request
from route.welcome import welcome_page
from route.homepage import homepage_page
from basic_mail_op import send_mail_op as smo
app = Flask(__name__)
app.register_blueprint(welcome_page)
app.register_blueprint(homepage_page)
smo.connect_to_mail_server()

@app.route('/',methods=['GET','POST'])
def hello_world():
    return '欢迎来到cs_304期末project'

@app.route('/test',methods=['GET','POST'])
def test():
    if(request.form.get('data1')=="我好牛逼"):
        return '你好牛逼'
    return '你不牛逼'


if __name__ == '__main__':
    app.run()

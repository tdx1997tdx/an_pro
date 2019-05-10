from flask import Flask, request
from route.homepage import homepage_page
from testing.email_test import email
app = Flask(__name__)
app.register_blueprint(homepage_page)

@app.route('/',methods=['GET','POST'])
def hello_world():
    return '欢迎来到cs_304期末project'

@app.route('/test',methods=['GET','POST'])
def test():
    if(request.form.get('data1')=="我好牛逼"):
        return '你好牛逼'
    return '你不牛逼'

@app.route('/test2',methods=['GET','POST'])
def test2():
    email.send_email()
    return '发送成功'

if __name__ == '__main__':
    app.run()

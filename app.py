from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    return 'hellow world'

@app.route('/test',methods=['GET','POST'])
def test():
    if(request.form.get('data1')=="我好牛逼"):
        return '你好牛逼'
    return '你不牛逼'


if __name__ == '__main__':
    app.run()

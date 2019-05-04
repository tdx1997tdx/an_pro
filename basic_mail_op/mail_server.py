import smtplib
import random
from basic_mail_op import temp_storage as ts
pass1='qimddlwbnympbfai'
pass2='pehiokuarlmibdcd'
def send_email(name,receiver):
    v_code = random.randint(1000, 9999)
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com',25)
    smtp.login('798637048@qq.com', pass2)
    message='Note Your Life验证码为:'+ str(v_code)
    try:
        smtp.sendmail('798637048@qq.com', receiver, message.encode('utf-8'))
    except:
        return False
    smtp.quit()
    ts.temp_storage[name]=v_code
    return True


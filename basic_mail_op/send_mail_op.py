import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header
from basic_mail_op import temp_storage as ts
pass1='qimddlwbnympbfai'
pass2='pehiokuarlmibdcd'

def send_email(name,receiver):
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com', 25)
    smtp.login('798637048@qq.com', pass2)
    print('邮箱服务连接成功')
    v_code = random.randint(1000, 9999)
    msg = 'Note Your Life的验证码为:' + str(v_code)
    message = MIMEText(msg, 'plain', 'utf-8')
    message['From'] = Header("Note Your Life的开发团队", 'utf-8')  # 发送者
    message['To'] = Header("尊敬的玩家", 'utf-8')  # 接收者
    message['Subject'] = Header('Note Your Life的验证码', 'utf-8')
    print(receiver)
    try:
        smtp.sendmail('798637048@qq.com', receiver, message.as_string())
        print('ok')
    except Exception as e:
        print(e)
        return False
    ts.temp_storage[name]=v_code
    smtp.close()
    return True


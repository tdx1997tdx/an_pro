import smtplib
from email.mime.text import MIMEText
from email.header import Header
from basic_mail_op.op_storage import storage
import random

class Email:

    def send_email(self,name,email_address):
        # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        v_code=random.randint(1000,9999)
        message = MIMEText('Note Your Life的验证码为:'+str(v_code), 'plain', 'utf-8')
        message['From'] = Header("Note Your Life的开发团队", 'utf-8')  # 发送者
        message['To'] = Header("尊敬的玩家", 'utf-8')  # 接收者
        subject = 'Note Your Life的验证码'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail('798637048@qq.com', email_address, message.as_string())
            storage.add(name,v_code)
            print('发送成功')
            return True
        except Exception as e:
            print(e)
            return False
import smtplib
from email.mime.text import MIMEText
from email.header import Header
pass1='qimddlwbnympbfai'
pass2='pehiokuarlmibdcd'
smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com',25)
print('连接成功')
smtp.login('798637048@qq.com', pass2)
print('登陆成功')
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Note Your Life的验证码为:5555', 'plain', 'utf-8')
message['From'] = Header("Note Your Life的开发团队", 'utf-8')  # 发送者
message['To'] = Header("尊敬的玩家", 'utf-8')  # 接收者
subject = 'Note Your Life的验证码'
message['Subject'] = Header(subject, 'utf-8')
#message='Note Your Life的验证码为:'+ str(5555)
smtp.sendmail('798637048@qq.com', '348398625@qq.com', message.as_string())
print('发送成功')
smtp.quit()
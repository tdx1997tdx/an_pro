import smtplib
pass1='qimddlwbnympbfai'
pass2='pehiokuarlmibdcd'
smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com',25)
print('连接成功')
smtp.login('798637048@qq.com', pass2)
print('登陆成功')
smtp.sendmail('798637048@qq.com', '348398625@qq.com','你好牛逼：2333333'.encode('utf-8'))
smtp.quit()
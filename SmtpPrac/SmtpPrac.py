# 发送邮件
# 导入包
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 配置邮件属性
mail_host = 'smtp.163.com'      # smtp服务
mail_sender = '18310684713@163.com'     # 发送方
mail_sender_password = 'haoyiran1372'   # 发送方密码（授权码）
mail_receiver = '844626764@qq.com'      # 接收方
mail_content = '一张图片'

# 创建一个附件实例
msg = MIMEMultipart()
msg['From'] = mail_sender
msg['To'] = mail_receiver
msg['Subject'] = Header('壁纸', 'utf-8')

# 邮件正文
msg.attach(MIMEText('这是我最喜欢的壁纸之一', 'plain', 'utf-8'))
# 构造附件
attachment_path = os.path.dirname(os.path.abspath(__file__)) + '\\' + 'J10.jpg'   # 附件路径
att = MIMEText(open(attachment_path, 'rb').read(), 'plain', 'utf-8')
att['Content-type'] = 'application/octet-stream'
# att['Content-Disposition'] = 'attachment;filename=J10.jpg'
att.add_header('Content-Disposition', 'attachment', filename=('gbk', '', '金甲猛龙.jpg'))
msg.attach(att)

# 发送邮件
try:
    s = smtplib.SMTP()
    s.connect(mail_host, 25)
    s.login(mail_sender, mail_sender_password)
    s.sendmail(mail_sender, mail_receiver, msg.as_string())
    print('发送成功')
except smtplib.SMTPException as message:
    print(message)



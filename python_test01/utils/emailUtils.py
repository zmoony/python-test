import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

# 邮件服务器域名（自行修改）
EMAIL_HOST = 'smtp.126.com'
# 邮件服务端口（通常是465）
EMAIL_PORT = 465
# 登录邮件服务器的账号（自行修改）
EMAIL_USER = 'xxxxxxxxx@126.com'
# 开通SMTP服务的授权码（自行修改）
EMAIL_AUTH = '邮件服务器的授权码'


def send_email(*, from_user, to_users, subject='', content='', filenames=[]):
    """发送邮件

    :param from_user: 发件人
    :param to_users: 收件人，多个收件人用英文分号进行分隔
    :param subject: 邮件的主题
    :param content: 邮件正文内容
    :param filenames: 附件要发送的文件路径
    """
    email = MIMEMultipart()
    email['From'] = from_user
    email['To'] = to_users
    email['Subject'] = subject

    message = MIMEText(content, 'plain', 'utf-8')
    email.attach(message)
    for filename in filenames:
        with open(filename, 'rb') as file:
            pos = filename.rfind('/')
            display_filename = filename[pos + 1:] if pos >= 0 else filename
            display_filename = quote(display_filename)
            attachment = MIMEText(file.read(), 'base64', 'utf-8')
            attachment['content-type'] = 'application/octet-stream'
            attachment['content-disposition'] = f'attachment; filename="{display_filename}"'
            email.attach(attachment)

    smtp = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
    smtp.login(EMAIL_USER, EMAIL_AUTH)
    smtp.sendmail(from_user, to_users.split(';'), email.as_string())
"""
邮件：
SMTP（简单邮件传输协议），它也是建立在 TCP 之上的应用级协议，
规定了邮件的发送者如何跟邮件服务器进行通信的细节。
Python 通过名为smtplib的模块将这些操作简化成了SMTP_SSL对象，通过该对象的login和send_mail方法，就能够完成发送邮件的操作。
"""
import random

import requests


def send_email():
    import smtplib
    from email.header import Header
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # 创建邮件主体对象
    email = MIMEMultipart()
    # 设置发件人、收件人和主题
    email['From'] = 'xxxxxxxxx@126.com'
    email['To'] = 'yyyyyy@qq.com;zzzzzz@1000phone.com'
    email['Subject'] = Header('上半年工作情况汇报', 'utf-8')
    # 添加邮件正文内容
    content = """据德国媒体报道，当地时间9日，德国火车司机工会成员进行了投票，
    定于当地时间10日起进行全国性罢工，货运交通方面的罢工已于当地时间10日19时开始。
    此后，从11日凌晨2时到13日凌晨2时，德国全国范围内的客运和铁路基础设施将进行48小时的罢工。"""
    email.attach(MIMEText(content, 'plain', 'utf-8'))

    # 创建SMTP_SSL对象（连接邮件服务器）
    smtp_obj = smtplib.SMTP_SSL('smtp.126.com', 465)
    # 通过用户名和授权码进行登录
    smtp_obj.login('xxxxxxxxx@126.com', '邮件服务器的授权码')
    # 发送邮件（发件人、收件人、邮件内容（字符串））
    smtp_obj.sendmail(
        'xxxxxxxxx@126.com',
        ['yyyyyy@qq.com', 'zzzzzz@1000phone.com'],
        email.as_string()
    )

def send_email_with_attachment():
    import smtplib
    from email.header import Header
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from urllib.parse import quote

    # 创建邮件主体对象
    email = MIMEMultipart()
    # 设置发件人、收件人和主题
    email['From'] = 'xxxxxxxxx@126.com'
    email['To'] = 'zzzzzzzz@1000phone.com'
    email['Subject'] = Header('请查收离职证明文件', 'utf-8')
    # 添加邮件正文内容（带HTML标签排版的内容）
    content = """<p>亲爱的前同事：</p>
    <p>你需要的离职证明在附件中，请查收！</p>
    <br>
    <p>祝，好！</p>
    <hr>
    <p>孙美丽 即日</p>"""
    email.attach(MIMEText(content, 'html', 'utf-8'))
    # 读取作为附件的文件
    with open(f'resources/王大锤离职证明.docx', 'rb') as file:
        attachment = MIMEText(file.read(), 'base64', 'utf-8')
        # 指定内容类型
        attachment['content-type'] = 'application/octet-stream'
        # 将中文文件名处理成百分号编码
        filename = quote('王大锤离职证明.docx')
        # 指定如何处置内容
        attachment['content-disposition'] = f'attachment; filename="{filename}"'
        email.attach(attachment)

    # 创建SMTP_SSL对象（连接邮件服务器）
    smtp_obj = smtplib.SMTP_SSL('smtp.126.com', 465)
    # 通过用户名和授权码进行登录
    smtp_obj.login('xxxxxxxxx@126.com', '邮件服务器的授权码')
    # 发送邮件（发件人、收件人、邮件内容（字符串））
    smtp_obj.sendmail(
        'xxxxxxxxx@126.com',
        'zzzzzzzz@1000phone.com',
        email.as_string()
    )

def send_message_by_luosimao(tel, message):
    """发送短信（调用螺丝帽短信网关）"""
    resp = requests.post(
        url='http://sms-api.luosimao.com/v1/send.json',
        auth=('api', 'key-注册成功后平台分配的KEY'),
        data={
            'mobile': tel,
            'message': message
        },
        timeout=10,
        verify=False
    )
    return resp.json()


def gen_mobile_code(length=6):
    """生成指定长度的手机验证码"""
    return ''.join(random.choices('0123456789', k=length))


def main():
    code = gen_mobile_code()
    message = f'您的短信验证码是{code}，打死也不能告诉别人哟！【Python小课】'
    print(send_message_by_luosimao('13500112233', message))


if __name__ == '__main__':
    main()

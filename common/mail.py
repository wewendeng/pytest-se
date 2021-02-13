import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


def send_mail(filename):
    """
    邮件发送函数，使用smtp
    """
    msg = MIMEMultipart()  # 带附件实例
    with open(filename, "rb") as fp:
        mail_body = fp.read()  # 读取报告文件内容
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))  # 邮件正文
    att = MIMEText(mail_body, "base64", 'utf-8')  # 附件格式
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename="report_test.html"'  # filename是附件名字
    msg.attach(att)

    msg['Subject'] = Header("接口自动化测试报告", 'utf-8')  # 邮件正文标题
    msg['from'] = 'xxx@xxx.com'  # 邮件发送者
    msg['to'] = "xxx1@163.com,xxx2@qq.com"  # 邮件接收者

    # 连接SMTP服务器，并发送邮件
    smtp = smtplib.SMTP()
    smtp.connect("smtp.exmail.qq.com")
    smtp.login("xxx@xxx.com", "abcdefghijk")  # 邮件发送者
    smtp.sendmail("xxx@xxx.com", msg['to'].split(','), msg.as_string())  # 邮件发送者
    smtp.quit()
    print('Email has send out !')
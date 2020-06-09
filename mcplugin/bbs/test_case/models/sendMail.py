from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib


def send_mail(fileName, receiver):
    smtpServer = 'smtp.163.com'
    user = 'qakkla@163.com'
    password = '2438675akkll'

    f = open(fileName, 'rb')
    mail_body = f.read()  # 读取报告
    f.close()

    subject = "自动化测试报告"
    att = MIMEText(mail_body, "html", "utf-8")
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename="new_test_report.html"'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = user
    msgRoot['To'] = receiver
    msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpServer)
    smtp.login(user, password)
    smtp.sendmail(user, receiver, msgRoot.as_string())
    smtp.quit()


def new_report(report_path):
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(report_path + '/' + fn))
    filename = os.path.join(report_path, lists[-1])
    return filename

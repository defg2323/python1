import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "defg2323@gmail.com" # gmail address
gmail_pwd = "dud&qnwk47" # gmail passw
#send_gmail("defg2323@naver.com", "메일제목", "안녕하세요")

def send_gmail(to, subject, text, attach):
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = to
msg['Subject'] = subject
msg.attach(MIMEText(text))
part = MIMEBase('application', 'octet-stream')
part.set_payload(open(attach, 'rb').read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
msg.attach(part)
mailServer = smtplib.SMTP("smtp.gmail.com", 587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(gmail_user, gmail_pwd)
mailServer.sendmail(gmail_user, to, msg.as_string())
mailServer.close()




i, hap = 0,0

for i in range(1, 101):
    if i % 3 == 0:
        continue

    hap += i

print("1~100의 합계(3의 배수 제외) : %d" % hap)


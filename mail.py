import smtplib

from local_config import mailtrap_username, mailtrap_password
from email.mime.text import MIMEText


def send_smtp_mail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'my_mail@mail.com'
    msg['To'] = 'your_mail@mail.com'

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as mailserver:
        mailserver.login(mailtrap_username, mailtrap_password)
        mailserver.sendmail(msg['From'], msg['To'], msg.as_string())

    print('email sent')

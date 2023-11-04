import os
import smtplib
import ssl
from email.mime.text import MIMEText


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = 'developmentandrzejr@gmail.com'
    password = os.getenv('PMCGooglePass')
    context = ssl.create_default_context()
    formatted_message = MIMEText(message, 'plain', 'utf-8')

    with smtplib.SMTP_SSL(host, port, context=context) as smtp:
        smtp.login(username, password)
        smtp.sendmail(username, username, formatted_message.as_string())

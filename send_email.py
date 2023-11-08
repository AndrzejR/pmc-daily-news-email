import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.message import EmailMessage


def send_email(subject, message):
    host = "smtp.gmail.com"
    port = 465
    username = 'developmentandrzejr@gmail.com'
    password = os.getenv('PMCGooglePass')
    context = ssl.create_default_context()

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['To'] = username
    msg['From'] = username
    # formatted_message = MIMEText(message, 'plain', 'utf-8')

    with smtplib.SMTP_SSL(host, port, context=context) as smtp:
        smtp.login(username, password)
        smtp.send_message(msg)

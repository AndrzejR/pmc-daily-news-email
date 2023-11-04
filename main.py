import requests
import os
import datetime
import smtplib
import ssl
import unicodedata


def send_news_email(articles):
    host = "smtp.gmail.com"
    port = 465
    username = 'developmentandrzejr@gmail.com'
    password = os.getenv('PMCGooglePass')
    context = ssl.create_default_context()

    message = ""
    for idx, article in enumerate(articles):
        message += str(idx + 1) + " " + article['title'] + "\n"
        message += article['description'] + "\n\n"
    message = message.encode("utf-8")
    message = f"""Subject: Daily News

    {message}
    """

    with smtplib.SMTP_SSL(host, port, context=context) as smtp:
        smtp.login(username, password)
        smtp.sendmail(username, username, message)


api_key = os.getenv("PMCNewsAPIKey")
topic = "Poland"
yesterday = datetime.date.today() - datetime.timedelta(days=1)

url = f"https://newsapi.org/v2/everything?\
q={topic}\
&from={yesterday}\
&sortBy=publishedAt\
&apiKey={api_key}"

response = requests.get(url)
content = response.json()
print(content)

send_news_email(content['articles'])

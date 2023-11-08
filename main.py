import requests
import os
import datetime
import send_email

NEWS_TOPIC = "marathon"
NR_OF_ARTICLES = 20
API_KEY = os.getenv("PMCNewsAPIKey")

yesterday = datetime.date.today() - datetime.timedelta(days=1)

url = f"https://newsapi.org/v2/everything?\
q={NEWS_TOPIC}\
&from={yesterday}\
&sortBy=publishedAt\
&apiKey={API_KEY}\
&language=en"

response = requests.get(url)
content = response.json()
articles = content['articles']

message = ""
for idx, article in enumerate(articles[:NR_OF_ARTICLES]):
    if article['title'] is not None:
        message = (message + str(idx + 1) + " "
                   + article['title'] + "\n"
                   + article['description'] + "\n"
                   + article['url'] + "\n\n")

send_email.send_email('Daily News', message)

import requests
import os
import datetime

api_key = os.getenv("PMCNewsAPIKey")
topic = "kosovo"
yesterday = datetime.date.today() - datetime.timedelta(days=1)

url = f"https://newsapi.org/v2/everything?\
q={topic}\
&from={yesterday}\
&sortBy=publishedAt\
&apiKey={api_key}"

response = requests.get(url)
content = response.json()

for article in content['articles']:
    print(article['title'])
    print(article['description'])

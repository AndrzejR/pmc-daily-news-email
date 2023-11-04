import requests
import os
import datetime
import send_email

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
articles = content['articles']

message = ""
for idx, article in enumerate(articles):
    message += str(idx + 1) + " " + article['title'] + "\n"
    message += article['description'] + "\n\n"
message = f"""Subject: Daily News

{message}
"""

send_email.send_email(message)

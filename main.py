import requests
import os

api_key = os.getenv("PMCNewsAPIKey")
topic = "kosovo"

url = f"https://newsapi.org/v2/everything?\
q={topic}\
&from=2023-10-28\
&to=from=2023-11-04\
&sortBy=publishedAt\
&apiKey={api_key}"

response = requests.get(url)
content = response.json()

for article in content['articles']:
    print(article['title'])
    print(article['description'])

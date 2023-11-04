import requests
import os

topic = "kosovo"
url = "https://newsapi.org/v2/everything?q=kosovo&from=2023-10-28&to=from=2023-11-04&sortBy=publishedAt&apiKey=e768b4d8baf14731b5b8f124ee08bca6"
api_key = os.getenv("PMCNewsAPIKey")


response = requests.get(url)
content = response.json()

for article in content['articles']:
    print(article['title'])
    print(article['description'])

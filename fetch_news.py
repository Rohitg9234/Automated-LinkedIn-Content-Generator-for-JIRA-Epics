import requests
import os

api_key= os.environ.get("NEWS_API")



def fetch_news_head(project):
    keywords = [project["title"], project["description"], " OR ".join(project["tags"])]
    search_query = " OR ".join(keywords)

    url = f'https://newsapi.org/v2/everything?q={search_query}&apiKey={api_key}&language=en&pageSize=3'

    response = requests.get(url)
    data = response.json()
    headlines = ""
    for article in data['articles']:
        #print("Title:", article['title'])
        headlines = headlines + " , " + article['title']

    return headlines

"""

project = {
    "id": 3,
    "title": "Zero Trust Security Rollout",
    "description": "Implement Zero Trust security across enterprise endpoints.",
    "status": "open",
    "contributors": [
      "Rajesh Gupta",
      "Meena Joshi"
    ],
    "tags": [
      "security",
      "zero-trust"
    ],
    "completion_date": 0,
    "content_generated": False
  }

print(fetch_news_head(project))
"""
import feedparser
import datetime

url="https://codeground.tistory.com"
feed = feedparser.parse(url+"/rss")

text = """
### Recent blog posts
"""

list = []


for i in feed["entries"]:
    dt = datetime.datetime.strptime(i["published"], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    text += f"[{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i["link"], i["title"])


f = open("README.md, mode=w", encoding="utf-8")
f.write(text)
f.close()
import requests
from bs4 import BeautifulSoup

req = requests.get("https://sports.news.naver.com/kbaseball/news/index.nhn?isphoto=N")
if req.status_code != 200 :
    print("failed", req.status_code)

html = req.text
bs = BeautifulSoup(html, "html.parser")

box = bs.find_all("div", class_="text")

newstitle = []
press = []
time = []

for b in box:
    newstitle.append(b.find("span").text)
    press.append(b.find("div", class_="source").find("span", class_="press").text)
    time.append(b.find("div", class_="source").find(text).text)

newsInfo = []
for i in range(len(box)) :
    news = []
    news.append(newstitle[i])
    news.append(press[i])
    news.append(time[i])
    newsInfo.append(news)

for i in newsInfo :
    print(i)
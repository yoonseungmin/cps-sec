import requests
from bs4 import BeautifulSoup

req = requests.get("https://movie.naver.com/movie/running/current.nhn#")
if req.status_code != 200 :
    print("failed", req.status_code)

html = req.text
bs = BeautifulSoup(html, "html.parser")

box = bs.find_all("dl", class_="lst_dsc")

title = []
ratio = []
book = []

for b in box:
    title.append(b.find("dt", class_="tit").find("a").text)
    ratio.append(b.find("div", class_="star_t1").find("span", class_="num").text)
    if b.find("dl", class_="info_exp") != None : 
        book.append(b.find("dl", class_="info_exp").find("span", class_="num").text)
    else : 
        book.append("0")

movieInfo = []
for i in range(len(box)) :
    movie = []
    movie.append(title[i])
    movie.append(ratio[i])
    movie.append(book[i])
    movieInfo.append(movie)

for i in movieInfo :
    print(i)
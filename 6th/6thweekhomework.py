from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "/6th/chromedriver.exe"
driver = webdriver.Chrome(path)

try :
    driver.get("https://sports.news.naver.com/esports/news/index.nhn?isphoto=N&page=1")
    time.sleep(1)

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    pages = bs.find("div", class_ = "paginate").find_all("a")[-1]["data-id"]
    pages = int(pages)
    
    title = []
    for i in range(pages) :
        driver.get("https://sports.news.naver.com/esports/news/index.nhn?isphoto=N&page=" + str(i + 1))
        time.sleep(3)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find("div", class_ = "news_list").find_all("div", class_ = "text")
        title.append("page" + str(i + 1))
        for c in conts :
            title.append(c.find("span").text)


finally :
    for t in title :
        if t.find("page") != -1 :
            print()
            print(t)
        else :
            print(t)
    driver.quit()
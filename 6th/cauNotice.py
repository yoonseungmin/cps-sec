from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "/6th/chromedriver.exe"

driver = webdriver.Chrome(path)

try : 
    driver.get("https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100#page1")
    time.sleep(1)

    html = driver.page_source # request.get().text
    bs = BeautifulSoup(html, "html.parser")

    pages = bs.find("div", class_ = "pagination").find_all("a")[-1]["href"].split("page")[1] #find_all은 list로 return해줘요
    #page247에서 247만 어떻게 얻느냐 -> split / 리스트 안에 있는 [1]이 두 번째 
    pages = int(pages)
    
    title = []
    for i in range(3) : #range(pages) :
        driver.get("https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100#page" + str(i + 1)) 
        #i에 int형 값들이 나오기 때문에 int값을 str으로 바꿔줌 리스트로 하는 걸 스트링으로 바꿔준다는 소린데 [range(pages)가 리스트임]
        #pages가 0번부터 시작하는 리스트이기 때문에 0번부터 시작하는 리스트에 1을 더해서 1번부터 시작 (페이지1부터 필요하니까)
        time.sleep(3)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find_all("div", class_ = "txtL")
        title.append("page" + str(i + 1))
        for c in conts :
            title.append(c.find("a").text)

finally :
    #time.sleep(3)
    for t in title :
        if t.find("page") != -1 :
            print()
            print(t)
        else :
            print(t)
    driver.quit()
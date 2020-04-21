import requests
from bs4 import BeautifulSoup

req = requests.get("http://www.personal-pack.com/shop/shopbrand.html?xcode=014&type=O")
if req.status_code !=200 :
    print("failed", req.status_code)

html = req.text

bs = BeautifulSoup(html, "html.parser")
box = bs.find_all("table", class_="product_table")

name = []
price = []

for b in box : 
    name.append(b.find("font", class_="brandbrandname").text)
    #price.append(b.find("td", class_="bandprice_tr").find("span", class_="brandprice").find("span", class_="mk_price").text)

shopInfo = []
for i in range(len(box)) :
    shop = []
    shop.append(name[i])
    #shop.append(price[i])
    shopInfo.append(shop)

for i in shopInfo :
    print(i)
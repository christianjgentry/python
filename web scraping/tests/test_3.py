import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.archdaily.com/')

soup = BeautifulSoup(r.text, 'html.parser')

data = soup.find_all("div", id="main")

_list = []


#print(soup.prettify())
for item in data:
    #print('######################################################################')
   #print(item.prettify())
    #print(item.find())
    
    for i in item.find_all("li", "afd-char-item"):
        #print(i.text.splitlines())
        print(i.text)





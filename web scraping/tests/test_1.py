from bs4 import BeautifulSoup

import requests

r  = requests.get('https://darksouls.wiki.fextralife.com/Dark+Souls+Remastered')

data = r.text

soup = BeautifulSoup(data, "lxml")

print(soup.get_text())

import requests
from lxml import html
import pandas as pd
from bs4 import BeautifulSoup

url = "http://econpy.pythonanywhere.com/ex/001.html"

resp = requests.get(url)
tree = html.fromstring(resp.content)

buyers = tree.xpath('//div[@title="buyer-name"]/text()')
prices = tree.xpath('//span[@class="item-price"]/text()')
df = pd.DataFrame()
df['Buyers'] = buyers
df['Cost'] = prices
print df
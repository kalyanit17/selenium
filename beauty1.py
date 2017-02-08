import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
resp = requests.get(url)
soup = BeautifulSoup(resp.text,"lxml")

table = soup.find('table',{'class' : 'wikitable sortable plainrowheaders' })
rows = table.find_all('tr')

A = []
B = []
C = []
D = []
E = []
F = []
G = []

for row in rows:
 cells = row.find_all('td')
 headers = row.find_all('th')
 if len(cells) == 6:
  A.append(cells[0].string)
  B.append(headers[0].string)
  C.append(cells[1].string)
  D.append(cells[2].string)
  E.append(cells[3].string)
  F.append(cells[4].string)
  G.append(cells[5].string)
  
df = pd.DataFrame(A,columns = ['Number'])
df['State/UT'] = B
df['Admin_Capital'] = C
df['Legislative_Capital'] = D
df['Judiciary_Capital'] = E
df['Year_Capital'] = F
df['Former_Capital'] = G
print df
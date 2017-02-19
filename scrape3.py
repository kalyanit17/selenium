import urllib2
import urllib
from bs4 import BeautifulSoup

url="https://www.google.co.in/?gfe_rd="+"python"+" "+"django"
req = urllib2.Request(url)
resp = urllib2.urlopen(req).read()
print resp
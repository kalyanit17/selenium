import webbrowser
import sys
import pyperclip
import requests
from lxml import html
from bs4 import BeautifulSoup

if len(sys.argv) > 1:
 address = ' '.join(sys.argv[1:])
else:
 address = pyperclip.paste()
 
webbrowser.open("https://www.google.com/maps/place/"+address)
urls = ['https://www.greatandhra.com','https://www.quora.com']
for url in urls:
 webbrowser.open_new_tab(url)
 

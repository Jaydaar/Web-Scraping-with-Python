from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as q

url = "http://www.nlcb.co.tt/"
webPage = q(url).read()
soup = bs(webPage, 'html.parser').encode('utf8')
print(soup)

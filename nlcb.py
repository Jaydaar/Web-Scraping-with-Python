from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as g
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,'utf8','backslashreplace')
url = "http://www.nlcb.co.tt/"
p = g(url)
soup = bs(p, 'html5lib')
print(soup.prettify())
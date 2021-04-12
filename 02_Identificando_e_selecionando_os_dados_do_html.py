#teste_alura

from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('http://alura-site-scraping.herokuapp.com/index.php')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html,'html.parser')
soup

cards = []
card = {}

anuncio = soup.find('div', {'class':'well card'}).get_text()
print(anuncio)


'''
url = 'http://alura-site-scraping.herokuapp.com/index.php'
response = urlopen(url)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html,'html.parser')
print(soup)
'''
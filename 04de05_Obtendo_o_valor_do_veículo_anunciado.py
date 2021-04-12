from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('http://alura-site-scraping.herokuapp.com/index.php')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html,'html.parser')
soup

cards = []
card = {}

anuncio = soup.find('div', {'class':'well card'})
#print(anuncio)
valor = anuncio.find('p',{'class':'txt-value'}).getText()
#print(valor)
card['value'] = valor
print(card)

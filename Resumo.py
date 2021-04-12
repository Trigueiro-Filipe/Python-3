from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://alura-site-scraping.herokuapp.com/'
response = urlopen(url)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html,'html.parser')
soup
#print(soup.h1)

cards = []
card = {}

anuncio = soup.find('div',{'class':'well card'})
anuncio


anuncio.find('div',{'class':'value-card'})

anuncio.find('p',{'class':'txt-value'}).getText()
card['value'] = anuncio.find('p',{'class':'txt-value'}).getText() #Essa parte vai usar no final
#print(card)

infos = anuncio.find('div',{'class':'body-card'}).findAll('p')
'''
for info in infos:
    print(info.get('class')[0].split('-')[-1],'-',info.get_text())
'''
for info in infos:
    card[info.get('class')[0].split('-')[-1]] = info.get_text()
    #print(card)

items = anuncio.find('div',{'class':'body-card'}).ul.findAll('li')
items
items.pop()
#print(items)
'''
for item in items:
	print(item.getText().replace('► ',''))
'''
acessorios = []
for item in items:
	acessorios.append(item.getText().replace('► ',''))
	#print(acessorios)

card['items'] = acessorios
#print(card)

#=====================================================
#Aula 12 do tópico 5
'''
image = anuncio.find('div',{'class':'image-card'}).img
#print(image)
#print(image.get('src'))
#print(image.get('src').split('/')[-1])
urlretrieve(image.get('src'), './webcrawler/output/img/' + image.get('src').split('/')[-1])
'''
#=====================================================
#Aula 02 do tópico 6    container-cards

#print(len(soup.find('div',{'id':'container-cards'}).findAll('div',class_='card')))
anuncios = soup.find('div',{'id':'container-cards'}).findAll('div',class_='card')

for anuncio in anuncios:
	print(str(anuncio) + '\n\n')

	



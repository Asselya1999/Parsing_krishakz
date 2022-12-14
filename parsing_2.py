import requests 
from bs4 import BeautifulSoup
from time import sleep 

# headers = {
# 	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 	'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36'
# }

def get_url():
	for count in range(1, 3): 
		url = f'https://krisha.kz/prodazha/kvartiry/almaty/?page={count}'
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'lxml')
		data = soup.find_all('div', class_='a-card__header-left')

		for i in data: 
			card_url = 'https://krisha.kz' + i.find('a').get('href')
			yield card_url 

def array():
	for card_url in get_url(): 
		print(card_url)
		response = requests.get(card_url)
		sleep(1)
		soup = BeautifulSoup(response.text, 'lxml')
		print('offer__advert-info' in response.text)

		with open('asd.txt', 'w', encoding="utf-8") as f:
			f.write(response.text)

		data = soup.find('div', class_='offer__advert-info')
		price = data.find(class_='offer__price').getText()
		
		rows = data.find_all('div', class_='offer__info-item')
		location = rows[0].getText() 
		type_building = rows[1].getText() 
		floor = rows[2].getText()

		yield price, location, type_building, floor
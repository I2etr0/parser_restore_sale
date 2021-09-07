import requests
from bs4 import BeautifulSoup

url = 'https://re-store.ru/discount/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
site = soup.find_all('div', class_='r-discount-table__row')

mas = []

for n, i in enumerate(site, 1):
    itemName = i.find_next('a', {'class': 'r-discount-table__product-name'}).text.strip()
    itemShop = i.find_next('div', {'class': 'r-discount-table__store-name js-show-store-popup'}).text.strip()
    itemNumber = i.find_next('a', {'class': 'r-discount-table__store-phone'}).text.strip()
    itemPrice = i.find_next('div', {'class': 'r-discount-table__product-price-current'}).text.strip()
    itemDescription = i.find_next('div', {'class': 'r-discount-table__product-description'}).text.strip()
    res = f'{n}: {itemName} в {itemShop}\nНомер телефона: {itemNumber}\nСтоимость: {itemPrice}\nПродается из-за {itemDescription}.\n\n '
    mas.extend(res)

result = ''.join(mas) + '\n' + 'URL: https://re-store.ru/discount/'
from bs4 import BeautifulSoup
import requests

source = requests.get('https://qefira.com').text
soup = BeautifulSoup(source, 'html.parser')

categories_soup = soup.find_all('div', class_ = 'home-categories__item')
titles = [category.find('span',class_='home-category__header__title').text.strip() for category in categories_soup]
links = [category.a['href'] for category in categories_soup]
count = [category.find('span', class_="home-category__cta__count").text.strip() for category in categories_soup]
subcat = [[x.text.strip('\n') for x in category.find_all('li', class_='home-category__list-item')] for category in categories_soup]

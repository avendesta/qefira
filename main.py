from bs4 import BeautifulSoup
import requests

source = requests.get('https://qefira.com').text
soup = BeautifulSoup(source, 'html.parser')

categories_soup = soup.find_all('div', class_ = 'home-categories__item')
# titles = [category.find('span',class_='home-category__header__title').text.strip() for category in categories_soup]
# links = [category.a['href'] for category in categories_soup]
# count = [int(category.find('span', class_="home-category__cta__count").text.strip()) for category in categories_soup]
# subcat = [[x.text.strip('\n') for x in category.find_all('li', class_='home-category__list-item')] for category in categories_soup]

def main_cats():
    cats = []
    for category in categories_soup:
        title = category.find('span',class_='home-category__header__title').text.strip()
        link = category.a['href']
        count = int(category.find('span', class_="home-category__cta__count").text.strip())
        subcats = [x.text.strip('\n') for x in category.find_all('li', class_='home-category__list-item')]
        cats.append( {
            'title':title,
            'link':link,
            'count':count,
            'subcats':subcats
        } )

    return cats

print(main_cats()[0])
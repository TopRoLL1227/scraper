import requests
from bs4 import BeautifulSoup

for count in range(1, 8):
    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={count}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('div', class_='caption')

    for laptop in data:
        model = laptop.find('a', class_='title').text
        description = laptop.find('p', class_='description').text.strip()
        print(f"Модель: {model}\nОпис: {description}\n")
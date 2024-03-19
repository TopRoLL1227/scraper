import requests
from bs4 import BeautifulSoup

for count in range(1, 8):
    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={count}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('div', class_='caption')

    for laptop in data:
        notebook = laptop.find('a', class_='title')
        model = notebook['title'] if 'title' in notebook.attrs else notebook.text.strip()
        description = laptop.find('p', class_='description').text.strip()
        print("Модель: " + model + "\n" + "Опис: " + description + "\n")




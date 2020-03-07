import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.mercadolibre.com.mx/')

soup = BeautifulSoup(response.content)

products = soup.find_all("div", {"class": "ui-item__content"})

products_data = []
for product in products:
    name = product.find("p", {"class": "ui-item__title"})
    price = product.find("span", {"class": "price-tag-fraction"})
    products_data.append({
        "name": name.string,
        "price": float(price.string.replace(',',''))
    })

print(products_data)
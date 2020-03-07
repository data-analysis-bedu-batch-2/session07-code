import requests
from bs4 import BeautifulSoup

response = requests.get('https://tendencias.mercadolibre.com.mx/')

soup = BeautifulSoup(response.content)

tendencias = soup.find_all("li", {"class": "searches__item"})

data = []
for tendencia in tendencias:
    anchor = tendencia.find("a")
    name = anchor.string
    link = anchor['href']
    data.append({
        "name": name,
        "link": link
    })

print(data)
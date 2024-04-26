import json
import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'https://www.olx.ua/uk/nedvizhimost/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
name = soup.find_all('h6', class_='css-16v5mdi er34gjf0')
price = soup.find_all('p', class_='css-tyui9s er34gjf0')
location = soup.find_all('p', class_='css-1a4brun er34gjf0')

data = {}
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
SQL = '''INSERT INTO quotes (_house_, _Price_, _Location_)
VALUES (?,?,?)'''
for _ in range(len(name)):
    cursor.execute(SQL, [name[_].text, price[_].text, location[_].text])
    print(name[_].text, price[_].text, location[_].text)
conn.commit()
conn.close()
for _ in range(len(name)):
    data[price[_].text] = {name[_].text: location[_].text.split()[1:] }
# print(response, soup)
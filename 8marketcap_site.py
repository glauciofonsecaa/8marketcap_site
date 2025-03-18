import requests
from bs4 import BeautifulSoup as bs

url = 'https://8marketcap.com/'
response = requests.get(url)

def gold():
    symbol = soup.select('#default-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > div:nth-child(2) > div:nth-child(1)')[0].text
    market_cap = soup.select('#default-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(5)')[0].text.replace('T', '')
    price = soup.select('#default-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(6)')[0].text
    var_24h = soup.select('#default-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > span:nth-child(1)')[0].text.strip()
    var_7d = soup.select('#default-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(8) > span:nth-child(1)')[0].text.strip()
    
    return symbol, market_cap, price, var_24h, var_7d

def apple():
    symbol = soup.select('#default-table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(3) > div:nth-child(2) > div:nth-child(1)')[0].text
    market_cap = soup.select('#default-table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(5)')[0].text.replace('T', '')
    price = soup.select('#default-table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(6)')[0].text
    var_24h = soup.select('#default-table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(7) > span:nth-child(1)')[0].text.strip()
    var_7d = soup.select('#default-table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(8) > span:nth-child(1)')[0].text.strip()
    
    return symbol, market_cap, price, var_24h, var_7d

if response.status_code == 200:
    soup = bs(response.content, 'html.parser')
    print(gold()[1])
    print(apple()[0])
    print(apple()[1])

else:
    print(f'Failure: {response.status_code}')
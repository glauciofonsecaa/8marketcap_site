import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

# URL da página
url = 'https://8marketcap.com/'

# Requisição HTTP para obter o conteúdo da página
response = requests.get(url)

# Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    soup = bs(response.content, 'html.parser')

    #Lista para armazenar os dados das criptomoedas
    crypto_data = []

    #Loop para buscar as 10 primeiras criptmoedas
    for i in range(1, 11):
        try:

            symbol_element = soup.select(f'#default-table > tbody:nth-child(2) tr:nth-child({i}) > td:nth-child(4) > span:nth-child(1)')[0]
            market_cap_element = soup.select(f'#default-table > tbody:nth-child(2) > tr:nth-child({i}) > td:nth-child(5)')[0]
            price_element = soup.select(f'#default-table > tbody:nth-child(2) > tr:nth-child({i}) > td:nth-child(6)')[0]
            var_24h_element = soup.select(f'#default-table > tbody:nth-child(2) > tr:nth-child({i}) > td:nth-child(7) > span:nth-child(1)')[0]
            var_7d_element = soup.select(f'#default-table > tbody:nth-child(2) > tr:nth-child({i}) > td:nth-child(8) > span:nth-child(1)')[0]

            symbol = symbol_element.text.strip()
            market_cap = market_cap_element.text.strip()
            price = price_element.text.strip()
            var_24h = var_24h_element.text.strip()
            var_7d = var_7d_element.text.strip()

            crypto_data.append([symbol, market_cap, price, var_24h, var_7d])
        except IndexError:
            print(f'Não foi possível encontrar os dados para a linha {i}')
            continue   

    # Criar DataFrame com os dados coletados
    df = pd.DataFrame(crypto_data, columns=['Symbol', 'Market Cap (T)', 'Price', '24h Change', '7d Change'])

    # Exibir DataFrame
    print(df.to_string(justify='center'))

else:
    print(f'Falha ao acessar o site. Status code: {response.status_code}')

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
    
    # Função para obter dados
    def get_data(row):
        symbol = soup.select(f'#default-table > tbody:nth-child(2) tr:nth-child({row}) > td:nth-child(4) > span:nth-child(1)')[0]
        market_cap = soup.select(f'#default-table > tbody:nth-child(2) > tr:nth-child({row}) > td:nth-child(5)')[0]
        price = soup.select(f'#default-table > tbody:nth-child(2) > tr:nth-child({row}) > td:nth-child(6)')[0]
        var_24h = soup.select(f'#default-table > tbody:nth-child(2) > tr:nth-child({row}) > td:nth-child(7) > span:nth-child(1)')[0]
        var_7d = soup.select(f'#default-table > tbody:nth-child(2) > tr:nth-child({row}) > td:nth-child(8) > span:nth-child(1)')[0]
        
        return symbol, market_cap, price, var_24h, var_7d

    # Coletar dados
    gold_data = get_data(1)
    apple_data = get_data(2)
    microsoft = get_data(3)
    nvidia = get_data(4)

    # Criar DataFrame
    df = pd.DataFrame([gold_data, apple_data, microsoft, nvidia], columns=['Symbol', 'Market Cap (T)', 'Price', '24h Change', '7d Change'])

    # Exibir DataFrame
    print(df)

else:
    print(f'Falha ao acessar o site. Código de status: {response.status_code}')

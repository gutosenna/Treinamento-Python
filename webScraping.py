import requests
from bs4 import BeautifulSoup

url = 'https://www.pichau.com.br/hardware/placa-de-video'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
placas = soup.find_all('div', class_='MuiCardContent-root jss334')
ultima_pagina = soup.find('button', class_='MuiButtonBase-root MuiPaginationItem-root MuiPaginationItem-page MuiPaginationItem-textPrimary Mui-selected MuiPaginationItem-sizeLarge')
placa = placas[0]
marca = placa.find('h2', class_='MuiTypography-root jss337 jss338 MuiTypography-h6').get_text().strip()
print(marca)

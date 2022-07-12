from time import sleep
import pandas as pd
import time
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

load_dotenv(dotenv_path=r'C:\Users\GUTO SENNA\PycharmProjects\CEMIG\arquivo.env')
local = r'C:\Users\GUTO SENNA\Downloads'

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://atende.cemig.com.br/Login')
navegador.find_element(By.ID, 'acesso').send_keys(os.environ["LOGIN_CEMIG"])
navegador.find_element(By.ID, 'senha').send_keys(os.environ["PASSWORD_CEMIG"])
sleep(10)
navegador.find_element(By.XPATH, '//*[@id="submitForm"]').click()
sleep(10)
matricula = ['3004304247', '3003759292', '3005570849', '3003302106', '3003302105',
             '3003302104', '3003586949', '3003744866', '3007669731', '3003262248',
             '3003586950', '3003303648', '3007648147', '3007547772',
             '3003570759', '3003278251', '3007242702', '3007332376', '3012026982']
# matricula = ['3004304247', '3003759292']
temp, lista = [], []
try:
    while True:
        for nInst in matricula:
            navegador.find_element(By.CLASS_NAME, 'input').send_keys(nInst)
            navegador.find_element(By.ID, 'pesquisaInstalacaoTop').click()
            sleep(15)
            navegador.find_element(By.XPATH, '//*[@id="divSegundaVia"]/div/div/div[1]/button').click()
            sleep(10)
            for i in range(1, 3):
                link = navegador.find_element(By.XPATH, f'//*[@id="tblGrid"]/tbody/tr[{i}]/td[6]/div/a').get_attribute(
                    'onclick')
                texto = navegador.find_element(By.XPATH, f'//*[@id="tblGrid"]/tbody/tr[{i}]/td[1]').text
                site = link.replace("BaixarPDF('/", "https://atende.cemig.com.br/").replace("', $(this));", "")
                print(texto, nInst, site)
                data = {
                    "Matricula": nInst,
                    'dataVencimento': texto,
                    "link": site
                }
                temp.append(data)
                # print(temp)
            lista = temp[:]
            navegador.find_element(By.ID, 'dropdownSelecionarInstalacao').click()
            navegador.find_element(By.ID, 'btnSelecionarOutraIN').click()
            sleep(10)
            if len(lista) / 2 == len(matricula):
                df = pd.DataFrame(data=lista)
                path = r"{}".format(local)
                try:
                    os.mkdir(path)
                except FileExistsError:
                    print(path, 'exits!')
                else:
                    print(path, 'created!')
                finally:
                    filepath = r"{}\cemig_hist_{}.csv".format(local, time.strftime("%Y%m%d-%H%M%S"))
                    df.to_csv(filepath, index=False)
                    print(filepath, 'created!')
                    navegador.close()
                break
        print(lista)
except:
    pass


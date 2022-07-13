from time import sleep
import pandas as pd
import time
from selenium import common
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from mes import mes_vencimento

# mes_desejado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

load_dotenv(dotenv_path=r'C:\Users\GUTO SENNA\PycharmProjects\CEMIG\arquivo.env')
local = r'C:\Users\GUTO SENNA\PycharmProjects\CEMIG\data'

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://atende.cemig.com.br/Login')
navegador.find_element(By.ID, 'acesso').send_keys(os.environ["LOGIN_CEMIG"])
navegador.find_element(By.ID, 'senha').send_keys(os.environ["PASSWORD_CEMIG"])
sleep(10)
navegador.find_element(By.XPATH, '//*[@id="submitForm"]').click()
sleep(10)
# matricula = ['3004304247', '3003759292', '3005570849', '3003302106', '3003302105',
#              '3003302104', '3003586949', '3003744866', '3007669731', '3003262248',
#              '3003586950', '3003303648', '3007648147', '3007547772',
#              '3003570759', '3003278251', '3007242702', '3007332376', '3012026982']
matricula = ['3004304247', '3003759292']
instList, newInstList, error = [], [], []
try:
    while True:
        for nInst in matricula:
            error = list()
            error.append(nInst)
            navegador.find_element(By.CLASS_NAME, 'input').send_keys(nInst)
            navegador.find_element(By.ID, 'pesquisaInstalacaoTop').click()
            sleep(15)
            navegador.find_element(By.XPATH, '//*[@id="divSegundaVia"]/div/div/div[1]/button').click()
            sleep(10)
            for i in range(1, 4):
                try:
                    link = navegador.find_element(By.XPATH, f'//*[@id="tblGrid"]/tbody/tr[{i}]/td[6]/div/a') \
                        .get_attribute('onclick')
                    texto = navegador.find_element(By.XPATH, f'//*[@id="tblGrid"]/tbody/tr[{i}]/td[1]').text
                    site = link.replace("BaixarPDF('/", "https://atende.cemig.com.br/").replace("', $(this));", "")
                    mes = mes_vencimento(texto)
                    data = {
                        "Matricula": nInst,
                        'Mes': mes,
                        'dataVencimento': texto,
                        "link": site
                    }
                    print(mes, texto, nInst, site)
                    instList.append(data)
                except common.exceptions.NoSuchElementException:
                    break
            newInstList = instList[:]
            if len(newInstList) / 2 == len(matricula):
                break
            navegador.find_element(By.ID, 'dropdownSelecionarInstalacao').click()
            navegador.find_element(By.ID, 'btnSelecionarOutraIN').click()
            sleep(10)
except common.exceptions.NoSuchElementException:
    print(f'Parou na matricula {error}')
    pass
finally:
    print(f'{len(newInstList) // 2} matriculas cadastradas e {len(newInstList)} links baixados')
    df = pd.DataFrame(data=newInstList)
    path = r"{}".format(local)
    try:
        os.mkdir(path)
    except FileExistsError:
        print(path, 'exits!')
    else:
        print(path, 'created!')
    filepath = r"{}\cemig_hist_{}.csv".format(local, time.strftime("%Y%m%d-%H%M%S"))
    df.to_csv(filepath, index=False)
    print(filepath, 'created!')
    navegador.close()
#########################
# mes.py
global mes


def mes_vencimento(txt):
    meses = ['', 'Janeiro', 'Fevereiro',
             'Março', 'Abril', 'Maio',
             'Junho', 'Julho', 'Agosto',
             'Setembro', 'Outubro', 'Novembro',
             'Dezembro']
    mes_venc = ['', '/02/', '/03/', '/04/', '/05/', '/06/', '/07/',
                '/08/', '/09/', '/10/', '/11/', '/12/', '/01/']
    for c in range(1, 13):
        if mes_venc[c] in txt:
            mes = meses[c]
            return mes


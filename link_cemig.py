from time import sleep
import pandas as pd
import time
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

load_dotenv(dotenv_path=r'C:\Users\Usuário\PycharmProjects\projetos_servico\CEMIG\arquivo.env')
local = r'G:\Meu Drive\SEÇÃO DE GESTÃO DE CONTRATOS\CEMIG - 2022\data'
mes = ''
error = []

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
instList, newInstList = [], []
try:
    while True:
        for nInst in matricula:
            error = []
            error.append(nInst)
            print(error)
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
                if '07' in texto:
                    mes = 'Junho'
                elif '06' in texto:
                    mes = 'Maio'
                data = {
                    "Matricula": nInst,
                    'Mes': mes,
                    'dataVencimento': texto,
                    "link": site
                }
                print(mes, texto, nInst, site)
                instList.append(data)
                # print(instList)
            newInstList = instList[:]
            if len(newInstList) / 2 == len(matricula):
                break
            navegador.find_element(By.ID, 'dropdownSelecionarInstalacao').click()
            navegador.find_element(By.ID, 'btnSelecionarOutraIN').click()
            sleep(10)
except:
    print(f'Parou na matricula {error}')
    pass
finally:
    print(len(newInstList), newInstList)
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

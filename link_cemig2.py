from time import sleep
import pandas as pd
import time
import selenium
from selenium import common
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from mes import mes_vencimento

# Seleciona as variáveis de ambiente no arquivo.env
load_dotenv(dotenv_path=r'C:\Users\Usuário\PycharmProjects\projetos_servico\CEMIG\arquivo.env')
local = r'C:\Users\Usuário\PycharmProjects\projetos_servico\CEMIG\data'

def main():
    while True:
        print('[1] - Globalizada\n[2] - Individual')
        escolha = int(input())
        if escolha == 1:
            globalizada()
        if escolha == 2:
            individual()
        else:
            print('Escolha errada')
            break


def individual():
    # Instala o webdriver Chrome
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get('https://atende.cemig.com.br/Login')
    # Define o tempo de espera máximo da requisição
    wait = WebDriverWait(navegador, 15)
    # Digita o usuario e senha
    wait.until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click()
    wait.until(EC.presence_of_element_located((By.ID, 'acesso'))).send_keys(os.environ["LOGIN_CEMIG"])
    wait.until(EC.presence_of_element_located((By.ID, 'senha'))).send_keys(os.environ["PASSWORD_CEMIG"])
    sleep(10) # Espera a validação do Captcha
    navegador.find_element(By.XPATH, '//*[@id="submitForm"]').click() # Clica no botão pra entrar no login
    sleep(10) # Espera entrar no login
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
                try:
                    wait.until(EC.presence_of_element_located((By.ID, 'limparInst'))).send_keys(nInst)
                except selenium.common.exceptions.TimeoutException:
                    sleep(10)
                    navegador.find_element(By.CLASS_NAME, 'NumeroInstalacao').send_keys(nInst)
                wait.until(EC.element_to_be_clickable((By.ID, 'pesquisaInstalacaoTop'))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="divSegundaVia"]/div/div/div[1]/button'))).click()
                sleep(10)
                for i in range(1, 4):
                    try:
                        link = navegador.find_element(By.XPATH, f'//*[@id="tblGrid"]/tbody/tr[{i}]/td[6]/div/a') \
                            .get_attribute('onclick')
                        venc = navegador.find_element(By.XPATH, f'//*[@id="tblGrid"]/tbody/tr[{i}]/td[1]').text
                        valor = navegador.find_element(By.XPATH, f'//*[@id="tblGrid"]/tbody/tr[{i}]/td[2]').text.replace('R$', '')
                        situacao = navegador.find_element(By.XPATH, f'//*[@id="tblGrid"]/tbody/tr[{i}]/td[3]').text.replace(' ', '_')
                        site = link.replace("BaixarPDF('/", "https://atende.cemig.com.br/").replace("', $(this));", "")
                        mes = mes_vencimento(venc)
                        data = {
                            "matricula": nInst,
                            'mesReferencia': mes,
                            'dataVencimento': venc,
                            'valor': valor,
                            'situacao': situacao,
                            "linkFaturas": site
                        }
                        print(nInst, mes, venc, 'R$'+ valor, situacao, site)
                        instList.append(data)
                    except selenium.common.exceptions.ElementClickInterceptedException:
                        continue
                    except common.exceptions.NoSuchElementException:
                        break
                newInstList = instList[:]
                if len(newInstList) / 2 == len(matricula):
                    break
                else:
                    navegador.find_element(By.ID, 'dropdownSelecionarInstalacao').click()
                    navegador.find_element(By.ID, 'btnSelecionarOutraIN').click()
                    sleep(10)
    except common.exceptions.NoSuchElementException:
        if matricula[0] in error:
            print('Concluído!')
        else:
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


def globalizada():
    # Instala o webdriver Chrome
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get('https://atende.cemig.com.br/Login')
    # Define o tempo de espera máximo da requisição
    wait = WebDriverWait(navegador, 15)
    # Digita o usuario e senha
    wait.until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click()
    wait.until(EC.presence_of_element_located((By.ID, 'acesso'))).send_keys(os.environ["LOGIN_CEMIG"])
    wait.until(EC.presence_of_element_located((By.ID, 'senha'))).send_keys(os.environ["PASSWORD_CEMIG"])
    sleep(10)  # Espera a validação do Captcha
    navegador.find_element(By.XPATH, '//*[@id="submitForm"]').click()  # Clica no botão pra entrar no login
    sleep(10)  # Espera entrar no login
    matricula = '3004304247'
    contrato = ['55708499']
    instList, newInstList, error = [], [], []
    try:
        while True:
            for nInst in contrato:
                error = list()
                error.append(contrato)
                try:
                    wait.until(EC.presence_of_element_located((By.ID, 'limparInst'))).send_keys(matricula)
                except selenium.common.exceptions.TimeoutException:
                    sleep(10)
                    navegador.find_element(By.CLASS_NAME, 'NumeroInstalacao').send_keys(matricula)
                wait.until(EC.element_to_be_clickable((By.ID, 'pesquisaInstalacaoTop'))).click()
                wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="divSegundaViaContaGlobalizada"]/div/div/div[1]/button'))).click()
                sleep(10)
                try:
                    wait.until(EC.presence_of_element_located((By.ID, 'numContaContrato'))).send_Keys(nInst)
                except AttributeError:
                    sleep(5)
                    navegador.find_element(By.ID, 'numContaContrato').send_keys(nInst)
                wait.until(EC.presence_of_element_located((By.ID, 'DataContrato'))).click()
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, '//*[@id="DataContrato"]/option[13]'))).click()
                for i in range(1, 4):
                    try:
                        link = navegador.find_element(By.XPATH, f'//*[@id="tblGrid"]/tbody/tr/td[6]/div/a') \
                            .get_attribute('onclick')
                        venc = navegador.find_element(By.XPATH, f'//*[@id="tblGrid"]/tbody/tr/td[2]').text
                        contrato = navegador.find_element(By.XPATH,
                                                       f'//*[@id="tblGrid"]/tbody/tr/td[1]').text
                        situacao = navegador.find_element(By.XPATH,
                                                          f'//*[@id="tblGrid"]/tbody/tr/td[4]').text.replace(' ',
                                                                                                                  '_')
                        site = link.replace("BaixarPDF('/", "https://atende.cemig.com.br/").replace("', $(this));", "")
                        mes = mes_vencimento(venc)
                        data = {
                            'contrato': contrato,
                            'mesReferencia': mes,
                            'dataVencimento': venc,
                            'situacao': situacao,
                            "linkFaturas": site
                        }
                        print(contrato, mes, venc, situacao, site)
                        instList.append(data)
                    except selenium.common.exceptions.ElementClickInterceptedException:
                        continue
                    except common.exceptions.NoSuchElementException:
                        break
                newInstList = instList[:]
                if len(newInstList) / 2 == len(contrato):
                    break
                else:
                    navegador.find_element(By.ID, 'dropdownSelecionarInstalacao').click()
                    navegador.find_element(By.ID, 'btnSelecionarOutraIN').click()
                    sleep(10)
    except common.exceptions.NoSuchElementException:
        if matricula[0] in error:
            print('Concluído!')
        else:
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
    # numContaContrato
    # DataContrato
    # buscar


if __name__ == '__main__':
    main()
    

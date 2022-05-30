import pandas as pd
import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1
# Passo 1 - Entrar no sistema da empresa
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(3)

# Passo 2 - Navegar no sistema até encontrar a base de dados
pyautogui.click(x=988, y=724, clicks=2) # time.sleep(5) # pyautogui.position()
time.sleep(2)

# Passo 3 - Exportat a base de vendas
pyautogui.click(x=1182, y=805)
pyautogui.click(x=3271, y=432)
pyautogui.click(x=2822, y=1450)
time.sleep(5)

# Passo 4 - Calcular os indicadores
tabela = pd.read_excel(r'C:\Users\GUTO SENNA\Downloads\Arquivo.xlsx')
print(tabela)

faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

# Passo 5 - Enviar email para a diretoria com os indicadores
pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://mail.google.com/mail/u/0/#inbox')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(5)

# clicar no botão escrever
pyautogui.click(x=263, y=439)
time.sleep(3)
# escrever destinatário
pyautogui.write('@email.com')
pyautogui.press('tab')
# escrever o assunto
pyautogui.press('tab')
pyperclip.copy('Relatórios de vendas')
pyautogui.hotkey('ctrl', 'v')
# escrever o corpo do e-mail
pyautogui.press('tab')
texto = f'''
Prezados, bom dia

O faturamento foi de R${faturamento:,.2f}
A quantidade foi {quantidade:,} de vendas

Att
Guto'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
# enviar o e-mail
pyautogui.hotkey('ctrl', 'enter')

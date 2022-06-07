# Exercício Python 114: Site está acessível?
# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import urllib
import urllib.request
try:
    response = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('erro')
else:
    print('ok')
    print(response.read())

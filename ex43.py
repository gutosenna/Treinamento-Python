peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
IMC = peso / (altura * altura)
print(f'Seu índece de Massa corporal é {IMC:.1f}')
if IMC < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= IMC < 25:
    print('Peso Ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 < IMC <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')

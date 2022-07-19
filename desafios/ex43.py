peso = float(input('Seu peso em quilos: '))
altura = float(input('Sua altura em metros: '))
IMC = peso / (altura ** 2)
print(f'Seu IMC é de: {IMC:.2f}')
if IMC < 18.5:
    print('\033[31mSeu peso está abaixo do ideal\033[m')
elif 18.5 <= IMC < 25:
    print('\033[32mSeu peso é ideal\033[m')
elif 25 <= IMC < 30:
    print('\033[33mVocê está em sobrepeso\033[m')
elif 30 <= IMC < 40:
    print('\033[34mVocê está em grau de obesidade\033[m')
else:
    print('\033[31mVocê está em grau de obesidade mórbida\033[m')



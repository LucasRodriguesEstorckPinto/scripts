import random
c = 0
print('---O computador pensou um número entre 0 e 10, é seu dever tentar descobrir esse número---')
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = random.choice(numeros)
resposta = int(input('digite aqui seu palpite:'))
while resposta != r:
    resposta = int(input('Que pena, tente novamente!!:'))
    c = c + 1
    if resposta < r:
        print('Mais... Tente novamente')
    elif resposta > r:
        print('Menos...Tente novamente')
print(f'Parabéns, você acertou depois de {c+1} tentativas')


print('O computador pensou um número entre 0 e 10, é seu dever tentar descobrir esse número')
import random
numeros = [1,2,3,4,5,6,7,8,9,10]
r = random.choice(numeros)
resposta = int(input('digite aqui seu palpite:'))

if resposta==r:
    print('Parabéns, você acertou')
else:
    print('Que pena, tente novamente')




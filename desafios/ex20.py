import random

p = input('Nome1:')

s = input('Nome2:')

t = input('Nome3:')

q = input('Nome4:')

escolha = [p, s, t, q]

random.shuffle(escolha)
print('A ordem de aprasentação será:',end=' ')
print(escolha)

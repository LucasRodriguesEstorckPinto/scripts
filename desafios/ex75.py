h1 =int(input(f'Digite um número: '))
h2 =int(input(f'Digite mais um número: '))
h3 =int(input(f'Digite outro número: '))
h4 =int(input(f'Digite o último número: '))
t = (h1,h2,h3,h4)
print('=-'*20)
print(f'            {t}')
print('=-'*20)
print(f'O número 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O valor 3 apareceu na {t.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ',end='')
for n in t:
    if n%2 ==0:
        print(n,end=' - ')
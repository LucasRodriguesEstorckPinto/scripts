n = int(input('Digite aqui um número: '))
contador = 0
for c in range(1, n + 1):
    if n % c == 0:
        contador = contador + 1

if contador == 2:
    print(f'O número {n} é um número primo')
else:
    print(f'O número {n} não é um número primo')


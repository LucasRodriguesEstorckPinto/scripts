a = int(input('Digite aqui um número:'))
b = int(input('Digite outro número:'))
c = [a, b]

if a > b:
    print(f'O primeiro valor é o maior: {max(c)}')
elif b > a:
    print(f'O segundo valor é o maior: {max(c)}')
else:
    print(f'Os valores {a} e {b} são iguais')

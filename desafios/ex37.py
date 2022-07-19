a = int(input('Digite aqui um número inteiro: '))
print('[1] BINÁRIO-')
print('[2] OCTAL-')
print('[3] HEXADECIMAL-')

b = int(input('Digite sua escolha: '))

if b == 1:
    print(bin(a)[2:])
elif b == 2:
    print(oct(a)[2:])
elif b == 3:
    print(hex(a)[2:])
else:
    print('Escolha inválida')

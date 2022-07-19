a = float(input('\033[1;31mInsira o comprimento A:\033[m'))
b = float(input('\033[1;31mInsira o comprimento B:\033[m'))
c = float(input('\033[1;31mInsira o comprimento C:\033[m'))

if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print(f'Os segmentos {a},{b} e {c}, PODEM formar um triângulo',end=' ')
    if a == b == c:
        print('EQUILÁTERO')  # TODOS OS LADOS IGUAIS
    elif a == b or b == c or a == c:
        print('ISÓSCELES')  # DOIS LADOS IGUAIS
    else:
        print('ESCALENO')  # TODOS OS LADOS DIFERENTES

else:
    print(f'Os segmentos {a},{b} e {c}, NÃO podem formar um triângulo')

a = float(input('\033[1;31mInsira o comprimento A:\033[m'))
b = float(input('\033[1;31mInsira o comprimento B:\033[m'))
c = float(input('\033[1;31mInsira o comprimento C:\033[m'))
resultado = True

if b - c < a < b + c:
    resultado = True
if a - c < b < a + c:
    resultado = True
if a - b < c < a + b:
    resultado = True
else:
    resultado = False

print(f'Os comprimentos podem formar um triângulo?')
print(resultado)
print('True=Sim ; False=Não')
from datetime import date
d = date.today().year
idade = 0
maiores = 0
menores = 0
for c in range(1,8):
    p = int(input(f'Digite aqui a data de nascimento da {c}° pessoa: '))
    idade = d - p
    if idade>=21:
        maiores= maiores+1
    else:
        menores = menores +1

print(f'Dentre as 7 pessoas lidas,{maiores} atingiram a maioridade e {menores} ainda não atingiram a maioridade')

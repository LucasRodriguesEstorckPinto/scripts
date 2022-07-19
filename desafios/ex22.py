nome = input('DIGITE AQUI O SEU NOME COMPLETO:').strip()
quan = nome.replace(" ", "")
let = nome.split()

print(f'Seu nome maiúsculo: {nome.upper()}')
print(f'Seu nome minúsculo: {nome.lower()}')
print(f'Quantidade de letras: {len(quan)}')
print(f'Seu primeiro nome tem {len(let[0])} letras')

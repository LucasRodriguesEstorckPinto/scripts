import unidecode
f = unidecode.unidecode(str(input('Digite aqui uma frase:')).strip().upper())
c = f.replace(' ','')
inv = c[::-1]
if inv==c:
    print(f'A frase {f} é um palíndromo: {inv}')
else:
    print(f'A frase {f} NÃO é um palíndromo: {inv}')
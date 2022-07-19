from datetime import date
dados = {}
dados['nome'] = str(input('Nome: ')).strip().lower().title()
dados['idade'] = date.today().year - int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho(0 se não tem): '))
if dados['ctps'] !=0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['aposentadoria'] = dados['idade'] - (date.today().year - dados['contratação'])  + 35
    dados['salário'] = float(input('Salário: R$ '))
print('-='*30)
for k , v in dados.items():
    print(f' - {k} tem o valor   {v}')

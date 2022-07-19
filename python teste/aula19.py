#pessoas = {'nome':'Lucas','sexo':'M' , 'idade':17}
#pessoas['peso'] = 54
#for k,v in pessoas.items():
#    print(f'{k} = {v}')
#brasil = []
#estado = {'uf':'Rio de Janeiro','sigla':'RJ'}
#estado2 = {'uf':'São Paulo','sigla':'SP'}
#brasil.append(estado)
#brasil.append(estado2)
#print(brasil[0]['sigla'])
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf']= str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for  v in e.values():
        print(v)
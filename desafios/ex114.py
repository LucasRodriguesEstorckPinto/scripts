import requests


def conectado(n):
    try:
        requests.get(n)
    except (requests.exceptions.InvalidSchema, requests.exceptions.InvalidURL):
        print('\033[31mO ENDEREÇO FOI DIGITADO INCORRETAMENTE\033[m')
    except requests.exceptions.MissingSchema:
        print('\033[31mFALTANDO CARACTERES NO ENDEREÇO\033[m')
    except requests.exceptions.ConnectionError:
        print('\033[33mVOCÊ NÃO ESTÁ CONECTADO A INTERNET/O SITE DIGITADO NÃO EXISTE OU ELE ESTÁ OFFLINE\033[m')
    except Exception as erro:
        print(f'\033[31mNÃO FOI POSSÍVEL SE CONECTAR AO SITE {n}\033[m')
    else:
        print(f'\033[32mO site {n} está acessível\033[m')


print('Exemplo de endereço de site: https://www.google.com/  siga esse modelo')
j = str(input('Digite o endereço de um site para conferir se está no ar: ')).strip().lower()
conectado(j)

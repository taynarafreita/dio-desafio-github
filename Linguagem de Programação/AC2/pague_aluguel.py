divida = int(input())
pagamento = int(input())
parcela = 1

while divida > 0:
    print(f'pagamento: {parcela}')
    print(f'antes = {divida}')
    parcela += 1
    if divida <= pagamento:
        divida = 0
        print(f'depois = {divida}')
    else:
        divida -= pagamento
        print(f'depois = {divida}')
    print('-----')

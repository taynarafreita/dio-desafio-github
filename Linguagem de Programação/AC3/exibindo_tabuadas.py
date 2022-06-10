numero_1 = int(input())
numero_2 = int(input())
if numero_1 <= numero_2:
    for c in range(numero_1, numero_2 + 1):
        for pos in range(1, 11):
            print(f'{c} x {pos} = {c * pos}')
        print('--' * 5)
else:
    print('Nenhuma tabuada no intervalo!')
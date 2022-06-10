numero = int(input())
numero_tabuada = 1

if not numero > 10:
    while numero_tabuada <= 10:
        total = numero * numero_tabuada
        print(f'{numero} x {numero_tabuada} = {total}')
        numero_tabuada += 1
else:
    print(f'Insira numeros de 1 até 10.')

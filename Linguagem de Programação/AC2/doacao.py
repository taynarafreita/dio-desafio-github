doacao = float(input())
soma = 0
real = soma * 2.50

while doacao != -1:
    soma = soma + doacao
    doacao = float(input())
    real = soma * 2.50
print(f'VC$ {soma:.2f}')
print(f'R$ {real:.2f}')

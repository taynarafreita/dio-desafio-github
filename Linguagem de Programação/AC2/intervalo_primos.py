inicio = int(input())
fim = int(input())
primos = 0

def eprimo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return num > 1

for numero in range(inicio, fim + 1):
    if eprimo(numero):
        print(numero)
        primos += 1
print(f'primos: {primos}')

tempo_gasto = []

while True:
    numero = int(input())
    if numero < 0:
        break
    tempo_gasto.append(numero)
media = sum(tempo_gasto) / len(tempo_gasto)
print(f'MEDIA: {media:.2f}')
for c in tempo_gasto:
    if c < media:
        print(c)

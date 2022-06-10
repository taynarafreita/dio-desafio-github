info = []
quantidade = int(input())
for c in range(0, quantidade):
    canais = input().split(';')
    info.append(canais)
bonusS = float(input())
bonusN = float(input())
print('-----')
print('BÔNUS')
print('-----')
for pos in info:
    print(f'{pos[0]}: R$ ', end='')
    if pos[3] == 'sim':
        print(f'{(float(pos[1]) // 1000) * bonusS + float(pos[2]):.2f}')
    elif pos[3] == 'não':
        print(f'{(float(pos[1]) // 1000) * bonusN + float(pos[2]):.2f}')

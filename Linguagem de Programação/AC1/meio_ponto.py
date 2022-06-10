trabalhos = float(input())
prova = float(input())
media = (trabalhos + prova) / 2

if media >= 6:
    print('aprovado')
elif trabalhos >= 2:
    print('talvez com a sub')
else:
    print('reprovado')

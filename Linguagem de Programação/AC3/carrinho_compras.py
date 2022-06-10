lista = list(map(int, input().split()))
resp = 0
while True:
    resp = input().split()
    if resp[0] == 'exibir':
        lista.sort()
        for pos, c in enumerate(lista):
            if pos == len(lista) - 1:
                print(c)
            else:
                print(c, end=' ')
    elif resp[0] == 'adicionar':
        lista.append(int(resp[1]))
    elif resp[0] == 'remover':
        if int(resp[1]) in lista:
            lista.remove((int(resp[1])))
        else:
            print(f'código {int(resp[1])} não encontrado')
    elif resp[0] == 'encerrar':
        lista.sort()
        for pos, c in enumerate(lista):
            if pos == len(lista) - 1:
                print(c)
            else:
                print(c, end=' ')
        break

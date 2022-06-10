alunos = int(input())

original = []
alterada = []
nota_corrigida = []
diferenca = 0

for c in range(alunos):
    nota = float(input())
    original.append(nota)

for c in range(alunos):
    nota = float(input())
    alterada.append(nota)
    if alterada[c] == 10 and original[c] != 10:
        diferenca += 1

print(f'NOTAS ALTERADAS: {diferenca}')

for c in range(alunos):
    if alterada[c] == 10 and original[c] != 10:
        nota_corrigida.append(original[c] + 2)
        if nota_corrigida[c] > 10:
            nota_corrigida[c] = 10.0
        print(f'*({c + 1:03d}) original: {original[c]:05.2f} | final: {nota_corrigida[c]:05.2f}')
    else:
        nota_corrigida.append(original[c])
        print(f'-({c + 1:03d}) original: {original[c]:05.2f} | final: {nota_corrigida[c]:05.2f}')


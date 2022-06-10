preco = float(input())
quantidade = int(input())

total = quantidade * preco

valor = 10 + quantidade
descontoEmPorcentagem = valor / 100

valorDesconto = total * descontoEmPorcentagem

print(f'{total:.2f}')
print(f'{total - valorDesconto:.2f}')

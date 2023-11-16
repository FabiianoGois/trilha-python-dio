valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

# Calcula o total dos hambúrgueres e das bebidas
totalHamburgueres = valorHamburguer * quantidadeHamburguer
totalBebidas = valorBebida * quantidadeBebida

# Calcula o preço final do pedido
precoFinalPedido = totalHamburgueres + totalBebidas

# Calcula o troco
troco = valorPago - precoFinalPedido

# Imprime a saída formatada
mensagem = f"O preço final do pedido é R$ {precoFinalPedido:.2f}. Seu troco é R$ {troco:.2f}."
print(mensagem)

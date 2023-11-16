valorPedido = float(input())

# Utilizando condicional para verificar se o valor do pedido é maior ou igual a R$ 50.00
if valorPedido >= 50:
    mensagem = "Parabéns, você ganhou uma sobremesa grátis!"
else:
    mensagem = "Que pena, você não ganhou nenhum brinde especial."

# Imprimindo a saída utilizando interpolação de strings
print(mensagem)

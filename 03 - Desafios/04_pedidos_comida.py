def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor

    # Cupom de desconto
    cupom = input().strip()
    desconto = 0.0

    if cupom == "10%":
        desconto = 0.10
    elif cupom == "20%":
        desconto = 0.20

    # Aplica o desconto ao valor total
    total_com_desconto = total * (1 - desconto)

    # Imprime o resultado formatado
    print(f"Valor total: {total_com_desconto:.2f}")

if __name__ == "__main__":
    main()

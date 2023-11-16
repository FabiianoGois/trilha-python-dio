numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input().lower() == 's'

    # Verifica se o prato é vegano ou não
    tipoVegano = "Vegano" if ehVegano else "Nao-vegano"

    # Imprime a saída formatada
    print(f"Pedido {i}: {prato} ({tipoVegano}) - {calorias} calorias")

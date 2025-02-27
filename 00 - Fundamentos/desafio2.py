import textwrap

def menu():
    menu = """
    ================== MENU ==================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuario
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"\n=== Depósito realizado com sucesso! Saldo atualizado: R$ {saldo} ===")
    else:
        print("\n@@@ Valor inválido para depósito. @@@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n @@@ Você não tem saldo suficiente para esse saque. @@@")
    elif excedeu_limite:
        print("\n @@@ O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n @@@ Número de saques excedido. Tente novamente amanhã. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Valor inválido para saque. @@@")
    
    return saldo, extrato

def exibir_extrato(saldo, /,*,extrato):
    print("\n ============ EXTRATO ============ ")
    print("Não foram realizadas movimentações. " if not extrato else extrato)
    print(f"Saldo: \t\tR$ {saldo:.2f}")
    print("\n ================================= ")

def novo_usuario(usuarios):
    cpf = input("Informe o CPF (Somente números.): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n @@@ Já existe usuário com esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero, bairro, cidade, estado): ")

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuario_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Conta criada com sucesso! ===")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    else:
        print("\n @@@ Usuário não encontrado! Fluxo de criação de conta encerrado! @@@")
        

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Nº da conta:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main(): 
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar(
                    saldo=saldo, 
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            novo_usuario(usuarios)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break

main()
        
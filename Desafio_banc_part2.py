def menu():    
    menu = """
    Selecione a opção desejada no MENU abaixo:
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Saldo na Tela
    [5] Nova Conta
    [6] Novo Usuário
    [7] Listar Contas
    [8] Sair
        """
    return input(menu)
    #return(input(menu1))
    #return input(textwrap.dedent(menu)) #este comando tabela pela identação do código, interessante de usar.

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    contas = []
    usuarios = []
    saldo = 0
    extrato = ""
    limite = 500
    numero_saques = 0

    while True:
        opcao = menu()

        if  opcao == "1":
            print("DEPÓSITO\n")
            valor = float(input("Informe o valor a ser depositado: "))

            saldo, extrato = depositar(saldo, valor, extrato)
      
        elif opcao == "2":
            valor = float(input("Informe o valor a ser sacado: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            saldo_tela(saldo)

        elif opcao == "5":
            numero_conta = len(contas) + 1    #ver este comando "len" onde é usado em listas para passar tipo vetor....
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
    
        elif opcao == "6":
            novo_usuario(usuarios)

        elif opcao == "7":
            listar_contas(contas)

        elif opcao == "8":
            print("Obrigado por utilizar nossos serviços!")    
            break

        else:
            print("Opção inválida, tente novamente")

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: {valor:.2f}\n"
        print("Depósito realizado com sucesso!!!")
    else:
        print("Depósito não realizado, valor inválido")
        return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo Insuficiente")
    elif excedeu_limite:
        print("Valor de saque indisponível")
    elif excedeu_saques:
        print("Número máximo de saques excedido")
    elif valor > 0:
        saldo -= valor
        extrato += f"saque: {valor:.2f}\n"
        print("Saque realizado com sucesso !")
    else:
        print("Saque não realizado, valor informado inválido")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("EXTRATO")
    print("Não foram realizado movimentações"if not extrato else extrato)
    print(f"\nSaldo: {saldo:.2f}\n")

def saldo_tela(saldo):
    print("Saldo atual é de:  {saldo:.2f}")

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado")

def novo_usuario(usuarios):
    cpf = input("Informe o número de seu CPF: ")
    usuario = filtrar_usuario(cpf, usuario)
    if usuario:
        print("CPF já cadastrado")
        return
    nome = input("Informe seu nome e sobrenome")
    data_nascimento = input("Informe a data de nascimento")
    endereco = input("Informe seu endereço")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
        Agência: {conta['AGENCIA']}
        C.Corrente: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

main()
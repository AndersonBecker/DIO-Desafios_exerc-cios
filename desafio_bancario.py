# Resolução do desafio

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Saldo na Tela
[5] Sair
"""
dep = ""
saldo = 0
extrato = ""
limite = 500
numero_saques = 3
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if  opcao == "1":
        print("DEPÓSITO")
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor  #valor sera adicionado junto ao saldo
            extrato += f"Depósito: R$ {valor:.2f}\n"    #string concatenada para consultar no extrato .2f é pra deixar o número com duas casas decimais
        else:
            print("Valor inválido, tente novamente.")
      
    elif opcao == "2":
        print("SACAR")
        valor = float(input("Informe o valor de saque: "))
        excedeu_saldo = valor > saldo          # Estes são verificadores de saques e limite.
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saque:
            print("Saldo não suficiente")
        elif excedeu_limite:
            print("Não autorizado, valor excede o limite!")
        elif excedeu_saques:
            print("Número máximo de saques excedido")
        elif valor > 0:
            saldo -= valor                 # <<<< Rever este bloco pra entender melhor
            extrato += f"Saque: R$  {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor informado inválido")    


    elif opcao == "3":
        print("EXTRATO")
        print("Não há movimentações registradas." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    
    elif opcao == "4":
        print(f"saldo atual é: R$ {saldo:.2f}")

    elif opcao == "5":
        print("Saindo do terminal")
        break

    else:
        print("Opção inválida, tente novamente.")
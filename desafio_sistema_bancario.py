#valor inteiro e positivo / extrato / msgs /
# limite diario saque 3 diario 500 reais / R$ xxx.xx

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
#numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Valor inválido! O valor do depósito deve ser positivo.")


    elif opcao == "s":
        if LIMITE_SAQUES > 0:
            valor = float(input("Informe o valor do saque: "))
        
            if valor > 0 and valor <= 500 and valor < saldo and valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                limite -= valor
                LIMITE_SAQUES -= 1
                print("Saque realizado com sucesso!")

            elif valor > 500:
                print("Valor inválido! O valor do saque excedeu o limite.")

            elif valor > saldo:
                print("Saldo indisponível!")

            elif valor > limite:
                print("Valor excede o limite disponível!")

            else:
                print("Valor inválido! O valor do saque deve ser positivo.")
        else:
            print("Limite diário de Saque excedido!")



    elif opcao == "e":
        print("\n============= Extrato =============")
    
        print("\nNão foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        
        print("\n===================================")


    elif opcao == "q": #tecla única para fechar o programa
        break


    else: #qlqr tecla anteriormente provavelmente era break, agr passa a ser else
        print("Operação inválida, por favor selecione novamente a operação desejada.")
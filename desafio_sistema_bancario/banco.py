menu = '''
[a] Depósito
[b] Saque
[c] Extrato
[d] Sair
'''

saldo = 0
LIMITE = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    opcao = input(menu)
    if opcao == "a":
        deposito = float(input(("Quanto deseja depositar? ")))
        if deposito <= 0:
            print("Valor incorreto inserido")
        else:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
    
    elif opcao == "b":
        saque = float(input(("Quanto deseja sacar? ")))
        if (saque > LIMITE or saque > saldo):
            print("É impossível sacar esse valor")
        else:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
    elif opcao == "c":
        print(f"""
=============== EXTRATO ===============
{extrato}

Saldo total: {saldo}
=======================================
              """)
    elif opcao == "d":
        break
    
    else: print("Operação inválida.")
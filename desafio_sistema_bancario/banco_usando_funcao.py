conta = 0
LIMITE_SAQUE = 500
num_saques = 0
NUM_MAX_SAQUES = 3
extrato = ""

def func_saque():
    #region Global's
    global conta
    global extrato
    global LIMITE_SAQUE
    global NUM_MAX_SAQUES
    global num_saques
    #endregion

    if num_saques >= NUM_MAX_SAQUES:
        print("Nao foi possível concluir essa ação pois o numero de saques foi excedido")
        return

    valor = int(input("\nDigite o valor a ser sacado: "))

    if valor > LIMITE_SAQUE:
        print("Nao e possivel sacar esse valor pois ele excede o limite de saque")
        return

    conta -= valor
    extrato += f"Saque: R$ {valor}\n"
    num_saques += 1



def func_deposito():
    #region Global's
    global conta
    global extrato
    #endregion
    
    valor = int(input("\nDigite o valor a ser depositado: "))
    conta += valor
    extrato += f"Deposito: R$ {valor}\n"

    
def func_extrato():
    global extrato
    global conta
    print(extrato)
    print(f"Valor em conta: R$ {conta}")

def func_exibir_menu():
    menu ="""
============ MENU ============
    1) Depositar
    2) Sacar
    3) Exibir Extrato
    4) Sair
    
    => """

    opcao = int(input(menu))
    return opcao

while(1):

    opcao = func_exibir_menu()

    if opcao == 1:
        func_deposito()
    elif opcao == 2:
        func_saque()
    elif opcao == 3:
        func_extrato()
    elif opcao == 4:
        break
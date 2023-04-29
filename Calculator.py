
def sum():

    conf = "SS"
    while(conf == 'SS'):
        try:
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite outro número: "))
        except:
            print("Erro! Digite um carácter válido!")
            break

        calc = n1 + n2
        print(f"{n1} + {n2} = {calc}")
        conf = input("Deseja continuar (S/N/SS)? ")
        conf = conf.upper()
        if conf == 'S':
            menu()


def subtraction():

    conf = "SS"
    while(conf == 'SS'):
        try:
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite outro número: "))
        except:
            print("Erro! Digite um carácter válido!")
            break

        calc = n1 - n2
        print(f"{n1} - {n2} = {calc}")
        conf = input("Deseja continuar (S/N/SS)? ")
        conf = conf.upper()
        if conf == 'S':
            menu()


def multiplication():

    conf = "SS"
    while(conf == 'SS'):
        try:
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite outro número: "))
        except:
            print("Erro! Digite um carácter válido!")
            break

        calc = n1 * n2
        print(f"{n1} * {n2} = {calc}")
        conf = input("Deseja continuar (S/N/SS)? ")
        conf = conf.upper()
        if conf == 'S':
            menu()


def potence():

    conf = "SS"
    while(conf == 'SS'):
        try:
            n1 = int(input("Digite a Base: "))
            n2 = int(input("Digite o Expoente: "))
        except:
            print("Erro! Digite um carácter válido!")
            break

        calc = n1 ** n2
        print(f"{n1} ^ {n2} = {calc}")
        conf = input("Deseja continuar (S/N/SS)? ")
        conf = conf.upper()
        if conf == 'S':
            menu()


def division():

    conf = "SS"
    while(conf == 'SS'):
        try:
            n1 = float(input("Digite um número: "))
            n2 = float(input("Digite outro número: "))
        except:
            print("Erro! Digite um carácter válido!")
            break

        calc = n1 / n2
        print(f"{n1} / {n2} = {calc}")
        conf = input("Deseja continuar (S/N/SS)? ")
        conf = conf.upper()
        if conf == 'S':
            menu()


def root():

    conf = "SS"
    while (conf == 'SS'):
        try:
            n1 = float(input("Digite o Radicando: "))
            n2 = float(input("Digite o Numerador: "))
            n3 = float(input("Digite o Denominador: "))
        except:
            print("Erro! Digite um carácter válido!")
            break

        calc = pow(n1, (n2/n3))
        print(f"Radicando: {n1}, Indice: {n3} = {round(calc, 3)}")
        conf = input("Deseja continuar (S/N/SS)? ")
        conf = conf.upper()
        if conf == 'S':
            menu()

def menu():
    print("""\n Manual(0)\n Soma(1) \n Subtrção(2) \n Multiplicação(3) \n Divisão(4) \n Potência(5)\n Raiz(6) \n""")
    print("SS: Continua na Mesma Operação")
    print("S: Continua Retorna Para o Menu")
    print("N: Encerra o Programa")

    select = input("Digite a opção desejada: ")

    try:
        select = int(select)
    except:
        print("Erro! Digite um carácter válido!")


    if select == 1:
        sum()

    if select == 2:
        subtraction()

    if select == 3:
        multiplication()

    if select == 4:
        division()


    if select == 5:
        potence()

    if select == 6:
        root()

menu()

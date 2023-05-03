def menu():
    opcao = int(input("Oque deseja realizar?\n " +
                      "1 - Criar login\n " +
                      "2 - Salvar login\n " +
                      "3 - Ver logins\n "))
    return opcao

def adicionar(dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número de funcionário: ")] = [
        input("Digite o nome do funcionário: "),
        input("Digite o cargo do funcionário: "),
        input("Digite o setor do funcionário: ")]
        resp = input("Digite <S> se deseja adicionar mais um funcionário: ").upper()

def registrar(dicionario):
    with open("tabela.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ";" + valor[0] + "; " + valor[1] + "; " + valor[2]+"" )
            return print("Funcionario registrado!")

def verificar():
    with open("tabela.txt", "r") as arquivo:
        lista = arquivo.readlines()
    return lista




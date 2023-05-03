from funcao import *
func = {}
opcao = menu()
while opcao > 0 and opcao < 4:
        if opcao == 1:
            adicionar(func)
            opcao = menu()
        elif opcao == 2:
            registrar(func)
            opcao = menu()
        elif opcao == 3:
            print(verificar())
            opcao = menu()

opcao = menu()




import os

passwords = {}

def managePasswords(passwords, passwordName):

    # Abra o arquivo (leitura)
    arquivo = open('passwords.txt', 'r')
    conteudo = arquivo.readlines()

    # insira seu conteúdo
    # obs: o método append() é proveniente de uma lista
    conteudo.append(str(passwords))

    # Abre novamente o arquivo (escrita)
    # e escreva o conteúdo criado anteriormente nele.
    arquivo = open('passwords.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()

exit = True
while(exit):

    print("O que deseja fazer? see / new / exit.")
    answer = input("Resposta:    ")

    if(answer == "new"):
        # to give name for password
        passwordName = input("Dê um nome à sua senha:  ")

        # get password
        newPassword = input("Insira sua nova senha: ")

        # keep password
        passwords[passwordName] = newPassword
        managePasswords(passwordName, newPassword)
        # clear shell
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Senha salva!")

    elif(answer == "see"):

        if(passwords == {}):
            # clear shell
            os.system('cls' if os.name == 'nt' else 'clear')

            print("\n")
            print("Você não tem senhas salvas!")
            print("\n")
        else:
            print("\n")
            # give back password
            x = passwords.items()
            for k, v in x:
                print(k + ": " + v)

            print("\n" * 2)

    elif(answer == "exit"):
        # clear shell
        os.system('cls' if os.name == 'nt' else 'clear')

        # get out
        exit = False

    else:
        print("Digite uma resposta válida!")
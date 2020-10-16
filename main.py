import os

passwords = {}

def managePasswords(passwords, passwordName):

    arquivo = open('passwords.txt', 'r')
    conteudo = arquivo.readlines()
    
    conteudo.append(str(passwords))

    arquivo = open('passwords.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()

def main(passwords):
    exit = True
    while(exit):

        print("What do you want to do? see / new / exit.")
        answer = input("Resposta:    ")

        if(answer == "new"):
            # to give name for password
            passwordName = input("Name your password:  ")

            # get password
            newPassword = input("Enter your new password: ")

            # keep password
            passwords[passwordName] = newPassword
            managePasswords(passwordName, newPassword)
            # clear shell
            os.system('cls' if os.name == 'nt' else 'clear')

            print("Password saved!")

        elif(answer == "see"):

            if(passwords == {}):
                # clear shell
                os.system('cls' if os.name == 'nt' else 'clear')

                print("\n")
                print("You don't have passwords saves!")
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
            print("Type a valid answer!")

main(passwords) # Run function

def menu_opcoes():
    print("\n" * 100)
    while True:
        print("\nBANCO DE DADOS: Turma de lógica de programação algoritímica!")
        print("\n      OPÇÕES DISPONÍVEIS NO BD:\n          1 - INSERIR\n          2 - PESQUISAR\n          3 - ALTERAR\n          4 - EXCLUIR\n          5 - LISTAR\n          6 - MEDIA DA TURMA\n          7 - SAIR\n")
        opcao = int(input("DÍGITE SUA OPÇÃO > "))
        if opcao == 1:
            inserir()
        elif opcao == 2:
            pesquisar()
        elif opcao == 3:
            alterar()
        elif opcao == 4:
            excluir()
        elif opcao == 5:
            listar()
        elif opcao == 6:
            media()
        elif opcao == 7:
            print("\n" * 100)
            print("\n\n>>>>>>> VOCÊ SAIU DO BANCO DE DADOS! <<<<<<<")
        else:
            print("\nOpção inválida, escolhas uma das 7 opções disponíveis para continuar!\n")


def inserir():
    #print("\n"*100)
    #print("\n     --- INSERÇÃO DE NOVO ALUNO NO BANCO DE DADOS ---\n")
    arquivo = open('banco_de_dados.txt','a+')
    nome = str(input("Digite o nome do aluno: ")).upper()
    nota1 = int(input("Digite a nota N° 01: "))
    nota2 = int(input("Digite a nota N° 02: "))
    #arquivo.writelines("\nMatricula.........: ")
    arquivo.writelines("Aluno.............: ")
    arquivo.writelines(str(nome) + "\n")
    arquivo.writelines("Nota N°01.........: ")
    arquivo.writelines(str(nota1) + "\n")
    arquivo.writelines("Nota N°02.........: ")
    arquivo.writelines(str(nota2) + "\n")
    media = (nota1 + nota2) / 2
    arquivo.writelines("Média.............: ")
    arquivo.writelines(str(media) + "\n")
    arquivo.writelines("Status do aluno...: ")
    if media > 7:
        status = "APROVADO"
    elif media >= 4:
        status = "EXAME FINAL"
    else:
        status = "REPROVADO"
    arquivo.writelines(str(status) + "\n")
    arquivo.write("\n----------------------------------------------------\n")
    arquivo.close()
    print("\n----------------------------------------------------\n            ALUNO CADASTRADO COM SUCESSO!\n----------------------------------------------------\n")
    continuar_cadastro = str(input("Desenha cadastrar outro aluno (S/N)? >>> ")).upper()
    if continuar_cadastro == "S":
        inserir()
    elif continuar_cadastro == "N":
        continuar_programa()
    

def listar():
    arquivo = open('banco_de_dados.txt','r')
    a = arquivo.readlines()
    for linha in a:
        linha = linha.rstrip()
        print(linha)
    arquivo.close()

def pesquisar():
    arquivo = open('banco_de_dados.txt','r')
    a = arquivo.readlines()
    aluno = input("\nDígite a matricula do aluno: ")
    for line in a:
        if aluno in line:
            posicao = (a.index(line))
            print("\n" + a[posicao].rstrip())
            print(a[posicao+1].rstrip())
            print(a[posicao+2].rstrip())
            print(a[posicao+3].rstrip())
            print(a[posicao+4].rstrip())
            print(a[posicao+5].rstrip())
    print("\nDeseja realizar uma nova pesquisa?") 
    cont = int(input("1 - SIM\n2 - MENU PRINCIPAL\nDigite sua escolha: "))              
    if cont == 1:
        pesquisar()
    elif cont == 2:
        menu_opcoes()
    else:
        print("Valor inválido, escolha uma das duas opções disponíveis")

def excluir():
    arquivo = open('banco_de_dados.txt', 'r+')
    a = arquivo.readlines()
    aluno = str(input("Dígite o nome do aluno que deseja excluir do banco de dados: ")).upper()
    for line in a:
        if aluno in line:
            posicao_aluno = (a.index(line))
            a[posicao_aluno] = ""
            a[posicao_aluno + 1] = ""
            a[posicao_aluno + 2] = ""
            a[posicao_aluno + 3] = ""
            a[posicao_aluno + 4] = ""
            arquivo = open('banco_de_dados.txt','w')
            arquivo.writelines(a)
    arquivo.close()

def continuar_programa():
    while True:
        print("\n>>> Dígite 1 para ir para ir para o menu principal.")
        print(">>> Dígite 2 para sair do Banco de dados.")
        continuar = int(input("Dígite sua opção: "))
        if continuar == 1:
            print("\n"*100)
            menu_opcoes()
        elif continuar == 2:
            print("\n"*100)
            print("\n\n>>>>>>> VOCÊ SAIU DO BANCO DE DADOS! <<<<<<<")
            break
        else:
             print("Valor inválido, digite 1 = Sim ou 2 = Não.")

def alterar():
    arquivo = open('banco_de_dados.txt','r+')
    a = arquivo.readlines()
    aluno = str(input("Dígite o nome do aluno que deseja fazer alterações: ")).upper()
    arquivo = open('banco_de_dados.txt', 'w')
    for line in a:
        if aluno in line:
            posicao_aluno = (a.index(line))
            novo_nome = str(input("Dígite o novo nome do aluno que deseja incluir: ")).upper()
            nova_nota1 = str(input("Nova primeira nota: "))
            nova_nota2 = str(input("Nova segunda nota: "))
            a[posicao_aluno] = (novo_nome)+"\n"
            a[posicao_aluno+ 1] = (nova_nota1) +"\n"
            a[posicao_aluno+ 2] = (nova_nota2) +"\n"
            arquivo.writelines(a)
    arquivo.close()
#print("\n"*15,"            BEM VINDO AO BANCO DE DADOS DA MATÉRIA DE LÓGICA DE PROGRAMAÇÃO ALGORITÍMICA!")
#input("                                    - APERTE ENTER PARA INICIAR -")
menu_opcoes()

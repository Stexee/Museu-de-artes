usuarioEsenha = {}
artes = {}
emprestimo = {}
def cadastrar_usuario():
    usuario = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
    nome_capitalizado = usuario.capitalize()
    usuarioEsenha[nome_capitalizado] = senha

    try:
        with open("usuarios.txt", "r", encoding="utf-8") as f:
            conteudo = f.read().strip()
    
    except Exception as e:
        print(f"Erro {e}")

        conteudo = ""
    
    with open("usuarios.txt", "w", encoding="utf-8") as f:
        if conteudo:
            f.write(conteudo + "\n")
        f.write(f"Usuário: {nome_capitalizado}")
    print(f"Usuario {nome_capitalizado} cadastrado com sucesso")

def logar_usuario():
    while True:
        usuario = input("Digite um nome de usuário: ")
        senha = input("Digite uma senha: ")
        nome_capitalizado = usuario.capitalize()
        if nome_capitalizado in usuarioEsenha and usuarioEsenha[nome_capitalizado] == senha:
            print(f"Bem vindo {nome_capitalizado}!")
            break
        else:
            print("Usuário ou senha incorreto.\n1- Tentar novamente\n2- Voltar")
            escolher = int(input("Digite de 1 a 2 para escolher: "))
            if escolher == 2:
                print("Voltando para o menu")
                break

def cadastrar_arte():
    titulo = input("Digite o titulo da arte: ")
    titulo_capitalizado = titulo.capitalize()
    autor = input("Digite o nome do autor: ")
    data = input("Digite a data de criação da arte: ")
    estilo = input("Digite o estilo artistico utilizado: ")
    tecnica = input("Digite a tecnica artistica utilizada: ")
    artes[titulo_capitalizado] = (f"\nautor:({autor})\nData de criação:({data})\nEstilo Artistico:({estilo})\nTecnica utilizada:({tecnica})\n____________________")


    try:
        with open("artes.txt", "r", encoding="utf-8") as f:
            conteudo = f.read().strip()
    
    except Exception as e:
        print(f"Erro {e}")

        conteudo = ""
    
    with open("artes.txt", "w", encoding="utf-8") as f:
        if conteudo:
            f.write(conteudo + "\n")
        f.write(f"{titulo_capitalizado}\nautor:({autor})\nData de criação:({data})\nEstilo Artistico:({estilo})\nTecnica utilizada:({tecnica})\n____________________\n")

    print(f"A arte {titulo_capitalizado} foi registrado com sucesso!")

def visualizar_usuarios():
    print(list(usuarioEsenha.keys()))

def visualizar_artes():
    for chave,valor in artes.items():
        print(f"{chave} {valor}")

def realizar_emprestimo():
    arte_desejada = input("Digite a arte desejada: ")
    nome_evento = input("Digite o nome do evento: ")
    data_emprestimo = input("Digite o periodo para o emprestimo: ")
    responsavel = input("Digite o nome do responsavel: ")
    emprestimo[arte_desejada] = (f"\nNome do evento: ({nome_evento})\nData de emprestimo: ({data_emprestimo})\nResponsavel: ({responsavel})")
    
    try:
        with open("emprestimos.txt", "r", encoding="utf-8") as f:
            conteudo = f.read().strip()
    
    except Exception as e:
        print(f"Erro {e}")

        conteudo = ""
    
    with open("emprestimos.txt", "w", encoding="utf-8") as f:
        if conteudo:
            f.write(conteudo + "\n")
        f.write(f"\nArte desejada: ({arte_desejada})\nNome do evento: ({nome_evento})\nData de emprestimo: ({data_emprestimo})\nResponsavel: ({responsavel})\n____________________\n")    

    if arte_desejada in artes:
        print("Pedido feito com sucesso!")
    else:
        print("Esse item não existe no sistema!")

def main():
    while True:
        print("------menu------")
        print("1- Cadastrar usuário\n2- Logar usuário\n3- Cadastrar arte\n4- Visualizar usuário\n5- Visualizar artes\n6- Realizar emprestimo\n7- Sair")
        escolha = int(input("Digite entre 1 e 6 para escolher: "))
        if escolha == 1:
            cadastrar_usuario()
        elif escolha == 2:
            logar_usuario()
        elif escolha == 3:
            cadastrar_arte()
        elif escolha == 4:
            visualizar_usuarios()
        elif escolha == 5:
            visualizar_artes()
        elif escolha == 6:
            realizar_emprestimo()
        elif escolha == 7:
            print("Saindo...")
            break
        else:
            print("Por favor, escolha apenas de 1 a 6!")
if __name__=="__main__":
    main()
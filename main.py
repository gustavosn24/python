livros = {}

#      cadrastro de livro      #
def cadastrar_livro():
    livro = {
        'titulo': input("Título: "),
        'autor': input("Autor: "),
        'anoPubli': int(input("Ano de Publicação: ")),
        'quantidade': int(input("quantidade: "))
    }
    
    titulo = livro["titulo"]

    if titulo in livros:
        print("livro já cadastrado!")
    else:
        livros[titulo] = livro
        print("livro cadrastado com suscesso!")



while True:
    print("--------------------")
    print(" Biblioteca Center ")
    print("--------------------")
    print(" 1 - Cadrastrar Livro")
    print(" 2 - Listar Livros")
    print(" 0 - Sair")
    opcao = int(input("escolha uma opção: "))

    if opcao == 1:
        cadastrar_livro()
    
    # elif opcao == 2:

        
    else:
        break

print(livros)

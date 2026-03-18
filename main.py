livros = {
    'metamoforse': {
        'titulo': 'metamoforse',
        'autor': 'gu',
        'anoPubli': 12,
        'quantidade': 3
    },
    'o rei': {
        'titulo': 'o rei',
        'autor': 'vc',
        'anoPubli': 23,
        'quantidade': 8
    },
    'dom casmurro': {
        'titulo': 'dom casmurro',
        'autor': 'machado de assis',
        'anoPubli': 1899,
        'quantidade': 5
    },
    '1984': {
        'titulo': '1984',
        'autor': 'george orwell',
        'anoPubli': 1949,
        'quantidade': 7
    },
    'o pequeno principe': {
        'titulo': 'o pequeno principe',
        'autor': 'antoine de saint-exupery',
        'anoPubli': 1943,
        'quantidade': 10
    }
}

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

def listar_livro():
    for i, (chave, valor) in enumerate(livros.items(), start=1):
        print(f"{i} - {chave}")



while True:
    print("--------------------")
    print(" Biblioteca Center ")
    print("--------------------")
    print(" 1 - Cadrastrar Livro")
    print(" 2 - Listar Livros")
    print(" 3 - Emprestimo de Livros")
    print(" 0 - Sair")
    opcao = int(input("escolha uma opção: "))

    if opcao == 1:
        cadastrar_livro()
    
    elif opcao == 2:
        print(" ")
        listar_livro()
        print(" ")
    
    # elif opcao == 3:

        
    else:
        break

print(livros)

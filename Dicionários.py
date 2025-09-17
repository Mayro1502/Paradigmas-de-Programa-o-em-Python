estoque = []


def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))

    produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
    estoque.append(produto)

    print(f"Produto '{nome}' adicionado com sucesso!\n")


def remover_produto():
    nome = input("Digite o nome do produto a ser removido: ")
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            estoque.remove(produto)
            print(f"🗑️ Produto '{nome}' removido com sucesso!\n")
            return
    print("Produto não encontrado!\n")


def listar_produtos():
    if not estoque:
        print("Estoque vazio!\n")
    else:
        print("\n--- Produtos em Estoque ---")
        for i, produto in enumerate(estoque, start=1):
            print(f"{i}. {produto['nome']} - Quantidade: {produto['quantidade']} - Preço: R${produto['preco']:.2f}")
        print()


def atualizar_produto():
    nome = input("Digite o nome do produto a ser atualizado: ")
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            print("Produto encontrado! (Deixe em branco para não alterar)")

            novo_nome = input("Novo nome: ")
            nova_quantidade = input("Nova quantidade: ")
            novo_preco = input("Novo preço: ")

            if novo_nome:
                produto["nome"] = novo_nome
            if nova_quantidade:
                produto["quantidade"] = int(nova_quantidade)
            if novo_preco:
                produto["preco"] = float(novo_preco)

            print("Produto atualizado com sucesso!\n")
            return
    print("Produto não encontrado!\n")


def menu():
    while True:
        print("==== MENU ====")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Listar produtos")
        print("4 - Atualizar produto")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            remover_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            atualizar_produto()
        elif opcao == "5":
            print("Saindo")
            break
        else:
            print("Opção inválida\n")

menu()
estoque = {'nome':'', 'preco':0.0, 'quantidade':0}


def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))
    produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
    estoque.append(produto)
    print(f"Produto '{nome}' adicionado com sucesso!\n")


def remover_produto():
    nome = input("Digite o nome do produto a ser removido: ")
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            estoque.remove(produto)
            print(f"Produto '{nome}' removido com sucesso!\n")
            return
    print("Produto não encontrado!\n")


def listar_produtos():
    if not estoque:
        print("Estoque vazio!\n")
    else:
        print("\n--- Produtos em Estoque ---")
        for i, produto in enumerate(estoque, start=1):
            print(f"{i}. {produto['nome']} - Quantidade: {produto['quantidade']} - Preço: R${produto['preco']:.2f}")
        print()


def atualizar_produto():
    nome = input("Digite o nome do produto a ser atualizado: ")
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            print("Produto encontrado! Deixe em branco caso não queira alterar.")
            novo_nome = input("Novo nome: ")
            nova_quantidade = input("Nova quantidade: ")
            novo_preco = input("Novo preço: ")

            if novo_nome:
                produto["nome"] = novo_nome
            if nova_quantidade:
                produto["quantidade"] = int(nova_quantidade)
            if novo_preco:
                produto["preco"] = float(novo_preco)

            print("Produto atualizado com sucesso!\n")
            return
    print("Produto não encontrado!\n")


def menu():
    while True:
        print("==== MENU ====")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Listar produtos")
        print("4 - Atualizar produto")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            remover_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            atualizar_produto()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!\n")


menu()
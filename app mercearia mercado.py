listadeprodutos =[]
#-----Começo cadastrarProduto-----
def cadastrarproduto(codigo):
    print(' Bem vindo ao cadastro de produtos')
    print('o codigo de produto a ser cadastrado é:{}'.format(codigo))
    produto = input('Digite o nome do produto:')
    fabricante = input('Digite a fabricante:')
    valor = float(input('Entre com o valor R$ do produto:'))
    dicionarioproduto = {'codigo' : codigo, 'produto':produto,'fabricante':fabricante,'valor' : valor}

    listadeprodutos.append(dicionarioproduto.copy())


#-----Fim cadastrarProduto--------

#-----Começo consultarProduto------
def consultarproduto():
    while True:
     try:
        print('bem vindo ao consultar produtos')
        opconsultar =int(input('Entre com a opção desejada:\n'
                               '1-Consultar todos os produtos\n'
                               '2-Consultar por codigo\n'
                               '3-Consultar por fabricante\n'
                               '4-retornar\n>>'))
        if opconsultar == 1:
          print('Bem vindo a consultar TODOS')
          for produto in listadeprodutos:
              for key, value in produto.items():
                  print('{} : {}'. format(key,value))
        elif opconsultar == 2:
            print('Bem vindo a consultar codigo')
            entrada = int(input('Digite o codigo desejado:'))
            for produto in listadeprodutos:
                if(produto['codigo']== entrada):
                    for key, value in produto.items():
                        print('{} : {}'.format(key, value))
        elif opconsultar == 3:
            print('Bem vindo a consultar fabricante')
            entrada = input('Digite o fabricante desejado:')
            for produto in listadeprodutos:
                if (produto['fabricante'] == entrada):
                    for key, value in produto.items():
                        print('{} : {}'.format(key, value))
        elif opconsultar == 4:
            return
        else:
            print('pare de digitar numeros que não existem no menu')
            continue




     except ValueError:
        print('Pare de digitar valores não inteiros')


#-----Fim consultarProduto--------

#-----Começo removerProduto---------
def removerproduto():
    print('bem vindo ao remover produto')
    entrada = int(input('Digite o codigo desejado:'))
    for produto in listadeprodutos:
        if (produto['codigo'] == entrada):
            listadeprodutos.remove(produto)
#-----Fim removerProduto--------

#-----Começo Main---------
print('bem vindo ao controle de estoque da mercearia de Lucas Garcia L. da Silva')
registroproduto = 0
while True:
    try:
        opcao = int(input('Digite a opção desejada:\n1-Cadastrar Produto\n2-Consultar Produto\n3-Remover Produto \n4-Sair\n>>'))
        if opcao == 1:
            registroproduto = registroproduto + 1
            cadastrarproduto(registroproduto)
        elif opcao == 2:
            consultarproduto()
        elif opcao == 3:
            removerproduto()
        elif opcao == 4:
            print('programa finalizado')
            break
        else:
            print('pare de digitar numeros que não existem no menu')
            continue
    except ValueError:
        print('Pare de digitar valores não inteiros')


#-----Fim Main--------

def cadastrarProduto (session):
    print('*******Iniciando cadastro do Produtos*******\n')
    codProd = input(str('Qual codigo do Produto? '))
    nomeProd = input(str('Qual nome do Produto? '))
    preco = input(str('Qual preço do Produto? '))
    desProd = input(str('Qual descrição do Produto? '))

    session.execute(" insert into produto (codProd, nomeProd, preco, descProd)values(%s,%s,%s,%s)", (codProd, nomeProd, preco, desProd))

    print('\Produto cadastrado com sucesso.')
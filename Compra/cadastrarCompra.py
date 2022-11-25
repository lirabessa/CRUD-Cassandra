def cadastrarCompra (session):
    print('*********Iniciando cadastro de compra*******\n')
    codCompra = input (str('Qual codigo do compra? '))
    nomeProd = input (str('Qual nome do Produto? '))
    nomeVend = input (str('Qual nome do Vendedor '))
    precoCompra = input (str('Qual preço da compra? '))

    session.execute(" insert into compra (codCompra, nomeProd, nomeVend, precoCompra)values(%s,%s,%s,%s)", (codCompra, nomeProd, nomeVend, precoCompra))

    print('\Compra cadastrada com sucesso.')
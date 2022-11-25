import Compra.buscarCompra as buscarCompra

def atualizarCompra (session):

    buscarCompra.procurarTodesCompra(session)

    codCompra = input(str('Qual o codigo da compra você quer atualizar? '))
    
    novoNomeProd = input (str('Qual nome do Produto? '))
    novoNomeVend = input (str('Qual nome do Vendedor? '))
    novoPrecoCompra = input (str('Qual preço da compra? '))

    session.execute("update compra set  nomeProd = %s, nomeVend  = %s, precoCompra  =%s where codCompra= %s",[novoNomeProd,novoNomeVend,novoPrecoCompra,codCompra])

    print('Atualizado com sucesso')
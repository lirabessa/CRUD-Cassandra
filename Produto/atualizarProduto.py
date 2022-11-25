import Produto.buscarProduto as buscarProduto

def atualizarProduto (session) :
    
    buscarProduto.procurarTodesProduto(session)

    codProd = input(str('Qual o cod do produto você quer atualizar? '))
    novoNomeProd = input (str('Qual novo nome do produto? '))
    novoPreco = input(str ('Qual novo preco do produto? '))
    novaDesProd = input(str ('Qual a nova descrição do produto? '))

    session.execute("update produto set nomeProd = %s, preco =%s, descProd =%s where codProd= %s",[novoNomeProd,novoPreco,novaDesProd,codProd])

    print('Atualizado com sucesso')
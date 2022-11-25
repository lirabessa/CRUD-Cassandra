from bson.objectid import ObjectId
import Compra.buscarCompra as buscarCompra

def atualizarCompra (session):
    minhaColuna = session.Compra
    buscarCompra.procurarTodesCompra(session)

    id = input(str('Qual o ID você quer atualizar? '))
    nomeProduto = input (str('Qual nome do Produto? '))
    valorProduto = input (str('Qual valor do Produto? '))
    nomeVendedor = input (str('Qual nome do Vendedor '))
    emailVendedor = input (str('Qual email do Vendedor? '))
    nomeUsuario = input (str('Qual nome do Usuario? '))
    emailUsuario = input (str('Qual email do Usuario? '))
    meuDicionario = { "$set":{ "produtos": {
        "nome": nomeProduto,
        "preco": valorProduto
    },
    "vendedor": {
        "nome": nomeVendedor,
        "email": emailVendedor
    },
    "usuario": {
        "nome": nomeUsuario,
        "email": emailUsuario
    },}}

    minhaColuna.update_one({'_id':ObjectId(id)}, meuDicionario)

    for x in minhaColuna.find():
        print(x)
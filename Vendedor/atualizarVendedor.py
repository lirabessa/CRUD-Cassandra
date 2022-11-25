from bson.objectid import ObjectId
import Vendedor.buscarVendedor as buscarVendedor

def atualizarVendedor (session):
    minhaColuna = session.vendedor
    buscarVendedor.procurarTodesVendedor(session)

    id = input(str('Qual o ID você quer atualizar? '))
    nome = input (str('Qual nome Vendedor? '))
    rua = input(str('Qual rua Vendedor? '))
    bairro = input(str ('Qual cep Vendedor? '))
    numero = input(str ('Qual cidade Vendedor? '))
    estado = input(str ('Qual estado Vendedor? '))
    cnpj = input(str ('Qual cnpj Vendedor? '))
    nomeProduto = input(str ('Qual nome do Produto que o Vendedor vende? '))
    valorProduto = input(str ('Qual valor do Produto? '))
    meuDicionario = { "$set":{ "nome": nome,
        "end": {
        "rua": rua,
        "bairro": bairro,
        "numero": numero,
        "estado": estado,         
    },
        "cnpj": cnpj,
        "produtos": {
        "nome": nomeProduto,
        "valor": valorProduto
    },}}

    minhaColuna.update_one({'_id':ObjectId(id)}, meuDicionario)

    for x in minhaColuna.find():
        print(x)
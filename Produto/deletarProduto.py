import Produto.buscarProduto as buscar

def deletarProduto (session):
    buscar.procurarTodesProduto(session)

    codProd = input(str('Qual o codigo do produto que você quer deletar? '))
    session.execute(f"delete from produto where codProd='{codProd}'")
    print(f"\n Produto do Codigo '{codProd} excluido")


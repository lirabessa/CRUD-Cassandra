import Compra.buscarCompra as buscar

def deletarCompra (session):
    buscar.procurarTodesCompra(session)

    codCompra = input(str('Qual o codigo da compra que você quer deletar? '))
    session.execute(f"delete from compra where codCompra='{codCompra}'")
    print(f"\n Compra do codigo '{codCompra} excluido")


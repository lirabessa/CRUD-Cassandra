import Vendedor.buscarVendedor as buscar

def deletarVendedor (session):
    buscar.procurarTodesVendedor(session)

    cpf = input(str('Qual o cpf do vendedor que você quer deletar? '))
    session.execute(f"delete from vendedor where cpf='{cpf}'")
    print(f"\n Vendedor do cpf '{cpf} excluido")



import Usuario.buscarUsuario as buscar

def deletarUsuario (session):
    
    buscar.procurarTodesUsuario(session)

    cpf = input(str('Qual o cpf do usuario que você quer deletar? '))
    session.execute(f"delete from usuario where cpf='{cpf}'")
    print(f"\n Usuario do cpf '{cpf} excluido")


import Usuario.buscarUsuario as buscarUsuario

def atualizarUsuario (session) :
    buscarUsuario.procurarTodesUsuario(session)

    cpf = input(str('Qual o email você quer deletar? '))
    novoNome = input(str('Digite o nome: '))
    novoEmail = input(str('Digite o endereço de email: '))
    novoTelefone = input(str('Digite o telefone: '))
    
    session.execute("update usuario set  nome = %s, email  = %s, telefone  =%s where cpf= %s",[novoNome,novoEmail,novoTelefone,cpf])


import Vendedor.buscarVendedor as buscarVendedor

def atualizarVendedor (session):
    
    buscarVendedor.procurarTodesVendedor(session)

    cpf = input(str('Qual o ID você quer atualizar? '))
    novoNome = input (str('Qual novo nome Vendedor? '))
    novoEmail = input(str('Qual novo email Vendedor? '))
    novoTelefone = input(str ('Qual novo telefone Vendedor? '))
    
    session.execute("update vendedor set  nome = %s, email  =%s, telefone  =%s where cpf= %s",[novoNome,novoEmail,novoTelefone,cpf])
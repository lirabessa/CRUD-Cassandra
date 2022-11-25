def cadastrarVendedor (session):
    
    cpf = input(str('Qual CPF Vendedor? '))
    nome = input (str('Qual nome Vendedor? '))
    email = input(str ('Qual email Vendedor? '))
    telefone = input(str ('Qual telefone Vendedor? '))
    
    session.execute(" insert into vendedor (cpf, nome, email, telefone)values(%s,%s,%s,%s)", (cpf, nome, email, telefone))

    print('\Vendedor cadastrado com sucesso.')
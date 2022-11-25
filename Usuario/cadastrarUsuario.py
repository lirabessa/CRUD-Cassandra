
def cadastrarUsuario(session):

    print('******Iniciando cadastro do usuario*****\n')

    cpf = input(str('Digite o cpf: '))
    nome = input(str('Digite o nome: '))
    email = input(str('Digite o endereço de email: '))
    telefone = input(str('Digite o telefone: '))
    session.execute(" insert into usuario (cpf, nome, email, telefone)values(%s,%s,%s,%s)", (cpf, nome, email, telefone))

    print('\nUsuario cadastrado com sucesso.')
def procurarTodesUsuario (session):
    for usuario in session.execute ('select * from usuario'):
        print (usuario)
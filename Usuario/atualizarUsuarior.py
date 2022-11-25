from bson.objectid import ObjectId
import Usuario.buscarUsuario as buscarUsuario

def atualizarUsuario (session) :
    buscarUsuario.procurarTodesUsuario(session)

    email = input(str('Qual o email você quer deletar? '))
    session.execute(f"update usuario set nome where email='{email}'")

    nome = input (str('Qual novo nome do Usuario? '))
    email = input(str ('Qual novo email Usuario? '))
  


def procurarTodesProduto (session):
      for produto in session.execute ('select * from produto'):
        print (produto)
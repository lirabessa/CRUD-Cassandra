def procurarTodesCompra (session):
      for compra in session.execute ('select * from compra'):
        print (compra)
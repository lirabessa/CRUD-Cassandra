
def procurarTodesVendedor (session):
      for vendedor in session.execute ('select * from vendedor'):
        print (vendedor)
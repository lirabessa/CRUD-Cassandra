def cadastrar (nome,rua,numero,cep,cidade,estado):
    global meuBanquinho 
    minhaColuna = meuBanquinho.Usuario
    print("FOOOOOI")
    meuDicionario = {"nome":nome,
     "endereco": {
        "Rua": rua,
        "numero":numero,
        "cep":cep,
        "cidade":cidade,
        "estado":estado       
    },}

    x =  minhaColuna.insert_one(meuDicionario)

    print(x.inserted_id)





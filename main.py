from multiprocessing.spawn import import_main_path
import Usuario.atualizarUsuarior as atualizarUsuario
import Usuario.buscarUsuario as buscarUsuario
import Usuario.cadastrarUsuario as cadastrarUsuario
import Usuario.deletarUsuario as deletarUsuario
import Produto.atualizarProduto as atualizarProduto
import Produto.buscarProduto as buscarProduto
import Produto.cadastrarProduto as cadastrarProduto
import Produto.deletarProduto as deletarProduto
import Vendedor.cadastrarVendedor as cadastrarVendedor
import Vendedor.buscarVendedor as buscarVendedor
import Vendedor.atualizarVendedor as atualizarVendedor
import Vendedor.deletarVendedor as deletarVendedor
import Compra.cadastrarCompra as cadastrarCompra
import Compra.buscarCompra as buscarCompra
import Compra.atualizarCompra as atualizarCompra
import Compra.deletarCompra as deletarCompra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'secure-connect-mercado-livre.zip'
}
auth_provider = PlainTextAuthProvider(
    'OpXSAeQTgsqEWcRYSoeJcPLu',
    '1TmFmAuuQBfBhEq8uX6RDf_Lj9xsJx_99.c5Fepyw-Gkbjf_+BAEmP2CoomW63rFvWKk-O,Sx8f6r_CMK9mGz8C2y8K3OfTSzaABYtUXMbDj5elkWthvJI2,tCjrqU39')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect('mercado_livre')
                    
row = session.execute("select release_version from system.local").one()

if row:
    print("Conectado")
    loop = True
    while loop:
        print('''  
        1 - CRUD Usuario \n 
        2 - CRUD Produto\n
        3 - CRUD Vendedor\n
        4 - CRUD Compra\n
        ''')
        opcao = input(str("Escolha uma opção para fazer o crud: "))
        match opcao:
            case '1':
                print('''  
                    1 - Cadastrar Usuario \n 
                    2 - Atualizar Usuario \n
                    4 - Buscar todos Usuarios \n
                    5 - Deletar Usuario \n
                    0 - Sair \n ''')
                opcaoUsuario = input(str("Escolha uma opção: "))
            
                match opcaoUsuario:
                    case '1':
                        cadastrarUsuario.cadastrarUsuario(session)
                    case '2':
                        atualizarUsuario.atualizarUsuario(session)
                    case '4':
                        buscarUsuario.procurarTodesUsuario(session)
                    case '5':
                        deletarUsuario.deletarUsuario(session)
                    case '0':
                        loop = False

            case '2':
                print('''  
                    1 - Cadastrar Produto \n 
                    2 - Atualizar Produto \n
                    4 - Buscar todos os Produtos \n
                    5 - Deletar Produtos \n
                    0 - Sair \n ''')
                opcaoProduto = input(str("Escolha uma opção: "))
            
                match opcaoProduto:
                    case '1':
                        cadastrarProduto.cadastrarProduto(session)
                    case '2':
                        atualizarProduto.atualizarProduto(session)
                    case '4':
                        buscarProduto.procurarTodesProduto(session)
                    case '5':
                        deletarProduto.deletarProduto(session)
                    case '0':
                        loop = False
                    
            case '3':
                print('''  
                    1 - Cadastrar Vendedor \n 
                    2 - Atualizar Vendedor \n
                    4 - Buscar todos os Vendedor \n
                    5 - Deletar Vendedor \n
                    0 - Sair \n ''')
                opcaoVendedor = input(str("Escolha uma opção: "))
            
                match opcaoVendedor:
                    case '1':
                        cadastrarVendedor.cadastrarVendedor(session)
                    case '2':
                        atualizarVendedor.atualizarVendedor(session)
                    case '4':
                        buscarVendedor.procurarTodesVendedor(session)
                    case '5':
                        deletarVendedor.deletarVendedor(session)
                    case '0':
                        loop = False
            

            case '4':
                print('''  
                    1 - Cadastrar Compra \n 
                    2 - Atualizar Compra \n
                    4 - Buscar todas as Compra \n
                    5 - Deletar Compra \n
                    0 - Sair \n ''')
                opcaoCompra = input(str("Escolha uma opção: "))
            
                match opcaoCompra:
                    case '1':
                        cadastrarCompra.cadastrarCompra(session)
                    case '2':
                        atualizarCompra.atualizarCompra(session)
                    case '4':
                        buscarCompra.procurarTodesCompra(session)
                    case '5':
                        deletarCompra.deletarCompra(session)
                    case '0':
                        loop = False
else:
    print("Houve um erro.")
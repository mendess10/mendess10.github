from cadastro.cadastrar_dados import cadastro_cliente, cadastro_fornecedor, cadastro_produto
from conexao_bd.conexao import inserir_projeto, conexao, inserir_responsavel, responsavel, associado, join_alvara_fornecedor

def cadastro_projeto():
    try:
        id_projeto = str(input("ID Projeto: ")).strip()
        bairro = str(input("Bairro: ")).strip()
        rua = str(input("Rua: ")).strip()
        cep = str(input("CEP: ")).strip()
        dimensao = str(input("Dimensão: ")).upper().strip()
        descricao = str(input("Descrição: ")).strip()
        tipo = str(input("Tipo: ")).upper().strip()
        n_alvara = str(input("N°ALVARA: ")).strip()
        orcamento = float(input("Orçamento: ").strip())
        data_entrega = str(input("Data de entrega: ")).strip()
        cpf_cliente = str(input("CPF do cliente: ")).strip()
        cau = str(input("CAU: ")).strip()

        try:
            conect = conexao()
            inserir_projeto(conect, id_projeto, bairro, rua, cep, dimensao, descricao, tipo, n_alvara, orcamento, data_entrega, cpf_cliente)
            inserir_responsavel(conect, cau, id_projeto)
            print(f"Projeto {id_projeto} cadastrado.")
        except Exception as e:
            print(f"Erro ao inserir projeto e responsável: {e}")
    except Exception as e:
        print(f"Erro ao coletar dados do projeto: {e}")

def meus_projetos():
    try:
        conect = conexao()
        responsavel(conect)
    except Exception as e:
        print(f"Erro ao listar projetos: {e}")

def meus_clientes():
    try:
        conect = conexao()
        associado(conect)
    except Exception as e:
        print(f"Erro ao listar clientes: {e}")

def funcao_arquiteto():
    try:
        while True:
            print("""------ARCTEC.COM------
                    1- Cadastrar Cliente
                    2- Cadastrar Projeto
                    3- Cadastrar Fornecedor
                    4- Cadastrar Produto
                    5- Meus Projetos
                    6- Meus Clientes
                    7- Join
                    8- Sair""")
            
            try:
                opcao = int(input("DIGITE A OPÇÃO DESEJADA: "))
                
                if opcao == 1:
                    cadastro_cliente()
                    continue
                elif opcao == 2:
                    cadastro_projeto()
                    continue
                elif opcao == 3:
                    cadastro_fornecedor()
                    continue
                elif opcao == 4:
                    cadastro_produto()
                    continue
                elif opcao == 5:
                    meus_projetos()
                    continue
                elif opcao == 6:
                    meus_clientes()
                    continue
                elif opcao == 7:
                    conect = conexao()
                    join_alvara_fornecedor(conect)
                elif opcao == 8:
                    break
                else:
                    print(f"""{opcao} NÃO existe.
                          Digite uma opção válida""")
                    break
            except Exception as e:
                print(f"Erro ao selecionar a opção: {e}")
    except Exception as e:
        print(f"Erro na função arquiteto: {e}")

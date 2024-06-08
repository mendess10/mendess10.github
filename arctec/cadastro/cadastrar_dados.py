from conexao_bd.conexao import conexao, inserir_cliente, inserir_fornecedor, inserir_produto, inserir_associado

def cadastro_cliente():
    try:
        cpf = str(input("CPF: ")).strip()
        nome = str(input("Nome: ")).upper().strip()
        sobrenome = str(input("Sobrenome: ")).upper().strip()
        telefone = str(input("Telefone: ")).strip()
        cau = str(input("CAU: ")).strip()

        try:
            conect = conexao()
            inserir_cliente(conect, cpf, nome, sobrenome, telefone, cau)
            inserir_associado(conect, cau, cpf)
        except Exception as e:
            print(f"Erro ao inserir cliente e associado: {e}")
    except Exception as e:
        print(f"Erro ao coletar dados do cliente: {e}")

def cadastro_fornecedor():
    try:
        cnpj = str(input("CNPJ: ")).strip()
        nome = str(input("Nome: ")).upper().strip()
        email = str(input("Email: ")).lower().strip()
        telefone = str(input("Telefone: ")).strip()
        descricao = str(input("Descrição: ")).strip()

        try:
            conect = conexao()
            inserir_fornecedor(conect, cnpj, nome, email, telefone, descricao)
        except Exception as e:
            print(f"Erro ao inserir fornecedor: {e}")
    except Exception as e:
        print(f"Erro ao coletar dados do fornecedor: {e}")

def cadastro_produto():
    try:
        marca = str(input("Nome: ")).upper().strip()
        tipo = str(input("Tipo: ")).upper().strip()
        quantidade = int(input("Quantidade: "))
        cnpj_fornecedor = str(input("CNPJ do Fornecedor: ")).strip()
        id_projeto = int(input("ID projeto: "))

        try:
            conect = conexao()
            inserir_produto(conect, marca, tipo, quantidade, cnpj_fornecedor, id_projeto)
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
    except Exception as e:
        print(f"Erro ao coletar dados do produto: {e}")

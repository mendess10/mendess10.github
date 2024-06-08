from conexao_bd.conexao import conexao, inserir_arquiteto, projetar_arquitetos, editar_arquiteto_nome, editar_arquiteto_sobrenome, editar_arquiteto_telefone, editar_arquiteto_email, editar_arquiteto_senha, deletar_arquiteto, login, deletar_login

def cadastro_arquiteto():
    try:
        cau = str(input("CAU: ")).strip()
        nome = str(input("Nome: ")).lower().strip()
        sobrenome = str(input("Sobrenome: ")).lower().strip()
        telefone = str(input("Telefone: ")).strip()
        email = str(input("Email: ")).lower().strip()
        senha = str(input("Senha: ")).strip()

        try:
            conect = conexao()
            inserir_arquiteto(conect, cau, nome, sobrenome, telefone, email, senha)
            login(conect, email, senha, cau)
        except Exception as e:
            print(f"Erro ao inserir arquiteto e login: {e}")
    except Exception as e:
        print(f"Erro ao coletar dados do arquiteto: {e}")

def listar_arquiteto():
    try:
        conect = conexao()
        projetar_arquitetos(conect)
    except Exception as e:
        print(f"Erro ao listar arquitetos: {e}")
    
def edicao_arquiteto():
    try:
        while True:
            print("""---EDITAR ARQUITETO---
                    1-Nome
                    2-Sobrenome
                    3-Telefone
                    4-Email
                    5-Senha""")
            opcao = int(input("Digite a opção desejada: "))

            try:
                conect = conexao()

                if opcao == 1:
                    editar_arquiteto_nome(conect)
                    continue
                elif opcao == 2:
                    editar_arquiteto_sobrenome(conect)
                    continue
                elif opcao == 3:
                    editar_arquiteto_telefone(conect)
                    continue
                elif opcao == 4:
                    editar_arquiteto_email(conect)
                    continue
                elif opcao == 5:
                    editar_arquiteto_senha(conect)
                    continue
                elif opcao == 6:
                    print("Saindo...")
                    break
                else:
                    print("Escolha uma opção desejada.")
                    continue
            except Exception as e:
                print(f"Erro ao editar arquiteto: {e}")
    except Exception as e:
        print(f"Erro ao iniciar edição de arquiteto: {e}")

def excluir_arquiteto():
    try:
        cau = str(input("CAU: ")).strip()
        try:
            conect = conexao()
            deletar_login(conect, cau)
            deletar_arquiteto(conect, cau)
        except Exception as e:
            print(f"Erro ao excluir arquiteto: {e}")
    except Exception as e:
        print(f"Erro ao coletar dados para exclusão de arquiteto: {e}")

def funcao_admin():
    try:
        while True:
            print("""ARCTEC.COM
                -------Admin-------
                1-Novo Arquiteto
                2-Meus arquitetos
                3-Editar
                4-Deletar
                5-Sair""")
            opcao = int(input("DIGITE A OPÇÃO DESEJADA: "))
            if opcao == 1:
                cadastro_arquiteto()
                continue
            elif opcao == 2:
                listar_arquiteto()
                continue
            elif opcao == 3:
                edicao_arquiteto()
                continue
            elif opcao == 4:
                excluir_arquiteto()
                continue
            elif opcao == 5:
                print("Saindo...")
                break
            else:
                print(f"""{opcao} NÃO existe.
                      Digite uma opção válida""")
                continue
    except Exception as e:
        print(f"Erro na função admin: {e}")

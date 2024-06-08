from paginas.pagina_arctec import funcao_arquiteto
from paginas.pagina_admin import funcao_admin
from conexao_bd.conexao import verificar_login, conexao
import getpass

try:
    conect = conexao()
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

while True:
    try:
        print("""------ARCTEC.COM------
        1-LOGIN
        2- SAIR""")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            valido = False
            while not(valido):
                try:
                    email = str(input("Email: "))
                    senha = getpass.getpass("Senha: ")
                    valido = verificar_login(email, senha)
                    if valido:
                        if "@admin" in email:
                            try:
                                funcao_admin()
                            except Exception as e:
                                print(f"Erro na função admin: {e}")
                        else: 
                            try:
                                funcao_arquiteto()
                            except Exception as e:
                                print(f"Erro na função arquiteto: {e}")
                    else:
                        print("Login inválido. Tente novamente.")
                except Exception as e:
                    print(f"Erro ao verificar login: {e}")
        elif opcao == 2:
            print("Saindo...")
            break
        else:
            print("Digite uma opção válida.")
            continue
    except Exception as e:
        print(f"Erro na seleção de opção principal: {e}")

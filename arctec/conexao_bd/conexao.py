import psycopg2
import bcrypt

def conexao():
    try:
        conect = psycopg2.connect(database="arctec",
                                  host="localhost",
                                  user="postgres",
                                  password="2501",
                                  port="5432")
        return conect
    except psycopg2.DatabaseError as e:
        raise Exception("Erro de conexão com o banco.") from e

def inserir_arquiteto(conexao, cau, nome, sobrenome, telefone, email, senha):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO arquiteto(cau, nome, sobrenome, telefone, email, senha) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (cau, nome, sobrenome, telefone, email, senha)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"Arquiteto {nome} adicionado.")
    except Exception as e:
        print(f"Erro ao inserir arquiteto: {e}")

def login(conexao, email, senha, cau):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO Login (email, senha, arquiteto_id) VALUES (%s, %s, %s)"
        valores = (email, senha, cau)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"Arquiteto(a) N°{cau} adicionado em login.")
    except Exception as e:
        print(f"Erro ao adicionar login: {e}")
    finally:
        cursor.close()
        conexao.close()

def inserir_cliente(conexao, cpf, nome, sobrenome, telefone, cau):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO cliente(cpf, nome, sobrenome, telefone, cau) VALUES (%s, %s, %s, %s, %s)"
        valores = (cpf, nome, sobrenome, telefone, cau)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"Cliente {nome} adicionado.")
    except Exception as e:
        print(f"Erro ao inserir cliente: {e}")

def inserir_fornecedor(conexao, cnpj, nome, email, telefone, descricao):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO fornecedor(cnpj, nome, email, telefone, descricao) VALUES (%s, %s, %s, %s, %s)"
        valores = (cnpj, nome, email, telefone, descricao)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"Fornecedor {nome} adicionado.")
    except Exception as e:
        print(f"Erro ao inserir fornecedor: {e}")

def inserir_produto(conexao, nome, tipo, quantidade, cnpj_fornecedor, projeto_id):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO produto(nome, tipo, quantidade, cnpj_fornecedor, projeto_id) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, tipo, quantidade, cnpj_fornecedor, projeto_id)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"Produto {nome} adicionado.")
    except Exception as e:
        print(f"Erro ao inserir produto: {e}")

def inserir_projeto(conexao, id_projeto, bairro, rua, cep, dimensao, descricao, tipo, n_alvara, orcamento, data_entrega, cpf_cliente):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO projeto(id_projeto, bairro, rua, cep, dimensao, descricao, tipo, n_alvara, orcamento, data_entrega, cpf_cliente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (id_projeto, bairro, rua, cep, dimensao, descricao, tipo, n_alvara, orcamento, data_entrega, cpf_cliente)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"Projeto {id_projeto} adicionado.")
    except Exception as e:
        print(f"Erro ao inserir projeto: {e}")

def inserir_associado(conexao, cau, cpf_cliente):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO associado(id_arquiteto, id_cliente) VALUES (%s, %s)"
        valores = (cau, cpf_cliente)
        cursor.execute(sql, valores)
        conexao.commit()
    except Exception as e:
        print(f"Erro ao inserir associado: {e}")

def inserir_responsavel(conexao, cau, id_projeto):
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO responsavel(id_arquiteto, id_projeto) VALUES (%s, %s)"
        valores = (cau, id_projeto)
        cursor.execute(sql, valores)
        conexao.commit()
    except Exception as e:
        print(f"Erro ao inserir responsável: {e}")

def deletar_login(conexao, cau):
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM login WHERE arquiteto_id = %s"
        valores = (cau,)
        cursor.execute(sql, valores)
        conexao.commit()
    except Exception as e:
        print(f"Erro ao deletar login: {e}")

def deletar_arquiteto(conexao, cau):
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM arquiteto WHERE cau = %s"
        valores = (cau,)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"Dados excluidos.")
    except Exception as e:
        print(f"Erro ao deletar arquiteto: {e}")

def projetar_arquitetos(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM arquiteto")
        resultado = cursor.fetchall()
        print(f"--MEUS ARQUITETOS--")
        for item in resultado:
            print(item)
        return resultado
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cursor is not None:
            conexao.close()

def editar_arquiteto_nome(conexao):
    try:
        cursor = conexao.cursor()
        valor = str(input(f"Digite o novo nome: ")).lower().strip()
        cau = str(input("CAU: ")).strip()
        sql = """UPDATE arquiteto
                SET nome = %s
                WHERE cau = %s"""
        valores = (valor, cau)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f" Arquiteto n°{cau} editado.")
    except Exception as e:
        print(f"Erro ao editar nome do arquiteto: {e}")

def editar_arquiteto_sobrenome(conexao):
    try:
        cursor = conexao.cursor()
        valor = str(input(f"Digite o novo sobrenome: ")).lower().strip()
        cau = str(input("CAU: ")).strip()
        sql = """UPDATE arquiteto
                SET sobrenome = %s
                WHERE cau = %s"""
        valores = (valor, cau)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f" Arquiteto n°{cau} editado.")
    except Exception as e:
        print(f"Erro ao editar sobrenome do arquiteto: {e}")

def editar_arquiteto_telefone(conexao):
    try:
        cursor = conexao.cursor()
        valor = str(input(f"Digite o novo telefone: ")).lower().strip()
        cau = str(input("CAU: ")).strip()
        sql = """UPDATE arquiteto
                SET telefone = %s
                WHERE cau = %s"""
        valores = (valor, cau)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f" Arquiteto n°{cau} editado.")
    except Exception as e:
        print(f"Erro ao editar telefone do arquiteto: {e}")

def editar_arquiteto_email(conexao):
    try:
        cursor = conexao.cursor()
        valor = str(input(f"Digite o novo email: ")).lower().strip()
        cau = str(input("CAU: ")).strip()
        sql = """UPDATE arquiteto
                SET email = %s
                WHERE cau = %s"""
        valores = (valor, cau)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f" Arquiteto n°{cau} editado.")
    except Exception as e:
        print(f"Erro ao editar email do arquiteto: {e}")

def editar_arquiteto_senha(conexao):
    try:
        cursor = conexao.cursor()
        valor = str(input(f"Digite a nova senha: ")).lower().strip()
        cau = str(input("CAU: ")).strip()
        sql = """UPDATE arquiteto
                SET senha = %s
                WHERE cau = %s"""
        valores = (valor, cau)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f" Arquiteto n°{cau} editado.")
    except Exception as e:
        print(f"Erro ao editar senha do arquiteto: {e}")

def verificar_login(email, senha):
    try:
        conn = conexao()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM Login WHERE email = %s AND senha = %s
        """, (email, senha))
        result = cursor.fetchone()
        return result is not None
    except Exception as e:
        print(f"Erro ao verificar login: {e}")
    finally:
        cursor.close()
        conn.close()

def responsavel(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM responsavel")
        resultado = cursor.fetchall()
        print(f"--MEUS PROJETOS--")
        for item in resultado:
            print(item)
        return resultado
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cursor is not None:
            conexao.close()

def associado(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM associado")
        resultado = cursor.fetchall()
        print(f"--MEUS CLIENTES--")
        for item in resultado:
            print(item)
        return resultado
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cursor is not None:
            conexao.close()

def join_alvara_fornecedor(conexao):
    try:
        cursor = conexao.cursor()
        sql = """
                SELECT p.n_alvara, f.nome
                FROM projeto p
                JOIN produto pr ON p.id_projeto = pr.projeto_id
                JOIN fornecedor f ON pr.cnpj_fornecedor = f.cnpj
            """
        cursor.execute(sql)
        resultados = cursor.fetchall()

        print("--Alvarás e Fornecedores--")
        for alvara, fornecedor in resultados:
            print(f"Número do Alvará: {alvara}, Nome do Fornecedor: {fornecedor}")
            
            
        return resultados
    except Exception as e:
        print(f"Erro ao realizar a junção: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if conexao is not None:
                conexao.close()

import mysql.connector

db_config = {
    'user':'natanhmc',
    'password':'1q2w3e4r5t',
    'host':'db4free.net',
    'database':'linkedin123',
    'port':3306
}

# Função para criar o banco de dados
def criarBanco():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INT PRIMARY KEY AUTO_INCREMENT,
            nome VARCHAR(50),
            perfil_linkedin VARCHAR(50)
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conexoes (
            id INT PRIMARY KEY AUTO_INCREMENT,
            contato1_id INT,
            contato2_id INT,
            FOREIGN KEY (contato1_id) REFERENCES contatos(id),
            FOREIGN KEY (contato2_id) REFERENCES contatos(id)
        );
    ''')

    conn.commit()
    conn.close()

# Função para adicionar um contato
def addContato(nome, perfil_linkedin):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM contatos WHERE nome = %s AND perfil_linkedin = %s", (nome, perfil_linkedin))
        contato_id = cursor.fetchone()

        if contato_id:
            contato_id = contato_id[0]
            print("Perfil já cadastrado !!")
        else:
            cursor.execute("INSERT INTO contatos (nome, perfil_linkedin) VALUES (%s, %s)", (nome, perfil_linkedin))

        conn.commit()
    except mysql.connector.Error as err:
        print(f"Erro ao adicionar contato: {err}")
    finally:
        if 'conn' in locals():
            conn.close()

# Função para alterar contatos
def alterarContato(id, novo_nome=None, novo_perfil=None):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        sql = '''UPDATE contatos SET
        nome=%s,
        perfil_linkedin=%s WHERE id=%s'''
        valores = (novo_nome, novo_perfil, id)
        cursor.execute(sql, valores)
        conn.commit()
    except mysql.connector.Error as err:
        
        print(f"Erro na atualização do contato: {err}")
    finally:
        if 'conn' in locals():
            conn.close()

# Função para listar contatos
def listarContatos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()

    conn.close()
    return contatos

# Função para adicionar uma conexão
def addConexao(contato1_id, contato2_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('BEGIN')
    
    try:
        cursor.execute('SELECT * FROM conexoes WHERE (contato1_id = %s AND contato2_id = %s) OR (contato1_id = %s AND contato2_id = %s)',
                      (contato1_id, contato2_id, contato2_id, contato1_id))

        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO conexoes (contato1_id, contato2_id) VALUES (%s, %s)', (contato1_id, contato2_id))
        else:
            print("A conexão entre esses contatos já existe.")
        
        conn.commit()
        
    except mysql.connector.Error as erro:
        conn.rollback()
        print(f"Ocorreu um erro {erro}. Tente novamente.")
        
    conn.close()

# Função para listar conexões de um contato
def listarConexoes(contato_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT contatos.nome
        FROM contatos
        JOIN conexoes ON contatos.id = CASE
            WHEN conexoes.contato1_id = %s THEN conexoes.contato2_id
            ELSE conexoes.contato1_id
        END
        WHERE conexoes.contato1_id = %s OR conexoes.contato2_id = %s
    ''', (contato_id, contato_id, contato_id))

    conexoes = cursor.fetchall()
    conn.close()
    return conexoes

def deletarContato(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM conexoes WHERE contato1_id = %s OR contato2_id = %s', (id, id))
    cursor.execute('DELETE FROM contatos WHERE id = %s', (id))

    conn.commit()
    conn.close()

def deletarConexao(id1, id2):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM conexoes WHERE (contato1_id = %s AND contato2_id = %s) OR (contato1_id = %s AND contato2_id = %s)', (id1, id2, id2, id1))

    conn.commit()
    conn.close()

# Função principal do menu
def menu():
    while True:
        print("\n1. Adicionar Contato")
        print("2. Alterar Contato")
        print("3. Listar Contatos")
        print("4. Adicionar Conexão")
        print("5. Listar Conexões de um Contato")
        print("6. Excluir contato")
        print("7. Excluir Conexão" )
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do contato: ")
            perfil_linkedin = input("Perfil do LinkedIn: ")
            addContato(nome, perfil_linkedin)
        elif escolha == "2":
            id = int(input("ID do contato a ser alterado: "))
            novo_nome = input("Novo Nome: ")
            novo_perfil_linkedin = input("Novo Perfil do LinkedIn: ")
            alterarContato(id, novo_nome, novo_perfil_linkedin)
        elif escolha == "3":
            contatos = listarContatos()
            print("Lista de Contatos:")
            for contato in contatos:
                print(f"ID: {contato[0]}, Nome: {contato[1]}, Perfil LinkedIn: {contato[2]}")
        elif escolha == "4":
            contato1_id = int(input("ID do primeiro contato: "))
            contato2_id = int(input("ID do segundo contato: "))
            addConexao(contato1_id, contato2_id)
        elif escolha == "5":
            contato_id = int(input("ID do contato: "))
            conexoes = listarConexoes(contato_id)
            print("Conexões do Contato:")
            for conexao in conexoes:
                print(conexao[0])
        elif escolha == "6":
            id = input("Informe o ID do contato a ser excluído: ")
            deletarContato(id)
        elif escolha == "7":
            id1 = input("Informe o ID do primeiro contato: ")
            id2 = input("Informe o ID do segundo contato: ")
            deletarConexao(id1, id2)
        elif escolha == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    criarBanco()
    menu()
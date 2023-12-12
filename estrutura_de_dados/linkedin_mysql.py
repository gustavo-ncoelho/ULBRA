import mysql.connector

db_config = {
    'user' : 'natanhmc',
    'password' : '1q2w3e4r5t',
    'host' : 'db4free.net',
    'database' : 'linkedin123',
    'port' : 3306
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
    2
    conn.commit()
    conn.close()

# Função para adicionar um contato
def adicionar_contato(nome, perfil_linkedin):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM contatos WHERE perfil_linkedin = %s', (perfil_linkedin,))
        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO contatos (nome, perfil_linkedin) VALUES (%s, %s)', (nome, perfil_linkedin))
            conn.commit()
        else:
            print("Contato já cadastrado.")
    except mysql.connector.Error as erro:
        print(f'Ocorreu um erro: {erro}. Tente novamente')
    
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
def adicionarConexao(contato1_id, contato2_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('BEGIN')

    try:
        cursor.execute('SELECT * FROM conexoes WHERE (contato1_id = %s AND contato2_id = %s) OR (contato2_id = %s AND contato1_id = %s)', (contato1_id, contato2_id, contato2_id, contato1_id))
        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO conexoes (contato1_id, contato2_id) VALUES (%s, %s)', (contato1_id, contato2_id))
        else:
            print('A conexão entre esses contatos já existe!!!')

        conn.commit()

    except mysql.connector.Error as erro:
        conn.rollback()
        print('Ocorreu um erro de concorrência. Tente novamente!!!')

    conn.close()

# Função para listar conexões de um contato
def listarConexoes (contato_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT contatos.nome
        FROM contatos
        JOIN conexoes ON contatos.id = CASE
            WHEN conexoes.contato1_id = %s THEN conexoes.contato2_id
            ELSE conexoes.contato1_id
        END
        WHERE conexoes.contato1_id = %s OR conexoes.contato2_id %s
        ''', (contato_id, contato_id, contato_id))
    
    conexoes = cursor.fetchall()
    conn.close()
    return conexoes

def excluirContato(contato_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM contatos WHERE id = %s', contato_id)

    conn.commit()
    conn.close()

# Função principal do menu
def menu():
    while True:
        print('''
            1. Adicionar Contato
            2. Listar Contatos
            3. Adicionar Conexão
            4. Listar Conexões de um Contato
            5. Remover um contato
            0. Sair 
        ''')

        opc = (input('Escolha uma opção: '))
        if opc == '1':
            nome = input('Nome do contato: ')
            perfil_linkedin = input('Perfil do Linkedin: ')
            adicionar_contato(nome,perfil_linkedin)
        elif opc == '2':
            contatos = listarContatos()
            print('Lista de Contatos: ')
            for contato in contatos:
                print(f'ID: {contato[0]}, Nome: {contato[1]}, Perfil LinkedIn: {contato[2]}')
        elif opc == '3':
            contato1_id = int(input('ID do primeiro contato: '))
            contato2_id = int(input('ID do segundo contato: '))
            adicionarConexao(contato1_id, contato2_id)
        elif opc == '4':
            contato_id = int(input('ID do contato: '))
            conexoes = listarConexoes(contato_id)
            print('Conexões do Contato: ')
            for conexao in conexoes:
                print(conexao[0])
        elif opc == '5':
            pass
        elif opc == '0':
            break
        else:
            print('Opção inválida. Tente novamente.')
            continue

if __name__ == '__main__':
    criarBanco()
    menu()  

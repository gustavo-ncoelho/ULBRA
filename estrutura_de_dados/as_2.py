import mysql.connector

class BancoDeDados:
    def __init__(self, db_config):
        self.db_config = db_config

    def conectar(self):
        return mysql.connector.connect(**self.db_config)

    def criar_tabelas(self):
        conn = self.conectar()
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

class ContatoManager:
    def __init__(self, db_config):
        self.db_config = db_config

    def adicionar_contato(self, nome, perfil_linkedin):
        try:
            conn = mysql.connector.connect(**self.db_config)
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

class Menu:
    def __init__(self, contato_manager):
        self.contato_manager = contato_manager

    def exibir_menu(self):
        while True:
            print("\n1. Adicionar Contato")
            print("2. Alterar Contato")
            print("3. Listar Contatos")
            print("4. Excluir contato")
            print("0. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                nome = input("Nome do contato: ")
                perfil_linkedin = input("Perfil do LinkedIn: ")
                self.contato_manager.adicionar_contato(nome, perfil_linkedin)
            elif escolha == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    db_config = {
        'user':'natanhmc',
        'password':'1q2w3e4r5t',
        'host':'db4free.net',
        'database':'linkedin123',
        'port':3306
    }

    banco = BancoDeDados(db_config)
    banco.criar_tabelas()

    contato_manager = ContatoManager(db_config)
    menu = Menu(contato_manager)
    menu.exibir_menu()
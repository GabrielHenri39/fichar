
import sqlite3

"""
>         ¥DRAGONAGE¥
           [ETERNO]

   Nome: 
   Idade: 
   HP:                 KI:
   ST:                  MP:
Fome: 100%
Sede:  100%
>          [SKILLS] 1pt
. 
.
.

>            ¥CORPO¥
       Cabeça:
       Corpo:
       Mao1:
       Mao2:
       Pernas:
       Pés:
      
 
>          [ATRIBUTOS] D20
. Força:  
. Resistência:
. Agilidade:
. Velocidade:
. Carisma:

>             ¥MENTE¥
   Ideais:
   
>       [CONHECIMENTOS] RP
.
.
.
             
>            [ATRIBUTOS] RP
.
.
.

>          ¥ESPIRITO¥
  KARNA:
  DARNA:

 
>           [ARQUÉTIPOS]
.
.
.
             
>          [ATRIBUTOS]
.
.
.

"""


class FichaDragonAge:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS personagem (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER,
                hp INTEGER,
                ki INTEGER,
                st INTEGER,
                mp INTEGER,
                fome INTEGER,
                sede INTEGER,
                skills INTEGER,
                corpo_id INTEGER,
                atributos_id INTEGER,
                mente_id INTEGER,
                FOREIGN KEY (corpo_id) REFERENCES corpo (id),
                FOREIGN KEY (atributos_id) REFERENCES atributos (id),
                FOREIGN KEY (mente_id) REFERENCES mente (id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS corpo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cabeca TEXT,
                corpo TEXT,
                mao1 TEXT,
                mao2 TEXT,
                pernas TEXT,
                pes TEXT,
                id_personagem INTEGER,
                FOREIGN KEY (id_personagem) REFERENCES personagem (id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS atributos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                forca INTEGER,
                resistencia INTEGER,
                agilidade INTEGER,
                velocidade INTEGER,
                carisma INTEGER,
                id_personagem INTEGER,
                FOREIGN KEY (id_personagem) REFERENCES personagem (id)
            )
            ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS mente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ideais TEXT
                id_personagem INTEGER,
                FOREIGN KEY (id_personagem) REFERENCES personagem (id)
                )
            ''')
        self.conn.commit()
        return self.conn
    
    def inserir_personagem(self, nome, idade, hp, ki, st, mp, fome, sede, skills):
        self.cursor.execute('''
            INSERT INTO personagem (nome, idade, hp, ki, st, mp, fome, sede, skills)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nome, idade, hp, ki, st, mp, fome, sede, skills))
        self.conn.commit()
        return self.cursor.lastrowid
    def inserir_corpo(self, cabeca, corpo, mao1, mao2, pernas, pes):
        self.cursor.execute('''
            INSERT INTO corpo (cabeca, corpo, mao1, mao2, pernas, pes)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (cabeca, corpo, mao1, mao2, pernas, pes))
        corpo_id = self.cursor.lastrowid
        self.conn.commit()
        return corpo_id
    def inserir_atributos(self, forca, resistencia, agilidade, velocidade, carisma):
        self.cursor.execute('''
            INSERT INTO atributos (forca, resistencia, agilidade, velocidade, carisma)
            VALUES (?, ?, ?, ?, ?)
        ''', (forca, resistencia, agilidade, velocidade, carisma))
        atributos_id = self.cursor.lastrowid
        self.conn.commit()
        return atributos_id
    def inserir_mente(self, ideais):
        self.cursor.execute('''
            INSERT INTO mente (ideais) VALUES (?)
        ''', (ideais,))
        mente_id = self.cursor.lastrowid
        self.conn.commit()
        return mente_id
    def recuperar_ficha(self, ficha_id):
        ficha_data = {}

        # Recupera os dados do personagem
        self.cursor.execute('''
            SELECT * FROM personagem WHERE id=?
        ''', (ficha_id,))
        personagem_data = self.cursor.fetchone()
        if personagem_data:
            ficha_data["personagem"] = {
                "nome": personagem_data[1],
                "idade": personagem_data[2],
                "hp": personagem_data[3],
                "ki": personagem_data[4],
                "st": personagem_data[5],
                "mp": personagem_data[6],
                "fome": personagem_data[7],
                "sede": personagem_data[8],
                "skills": personagem_data[9]
            }

            corpo_id = personagem_data[10]
            atributos_id = personagem_data[11]
            mente_id = personagem_data[12]

            # Recupera os dados do corpo
            self.cursor.execute('''
                SELECT * FROM corpo WHERE id=?
                ''', (corpo_id,))
            corpo_data = self.cursor.fetchone()
            if corpo_data:
                ficha_data["corpo"] = {
                    "cabeca": corpo_data[1],
                    "corpo": corpo_data[2],
                    "mao1": corpo_data[3],
                    "mao2": corpo_data[4],
                    "pernas": corpo_data[5],
                    "pes": corpo_data[6]
                }
            self.cursor.execute('''
                SELECT * FROM atributos WHERE id=?
                ''', (atributos_id,))
            atributos_data = self.cursor.fetchone()
            if atributos_data:
                ficha_data["atributos"] = {
                    "forca": atributos_data[1],
                    "resistencia": atributos_data[2],
                    "agilidade": atributos_data[3],
                    "velocidade": atributos_data[4],
                    "carisma": atributos_data[5]
                }
            self.cursor.execute('''
                SELECT * FROM mente WHERE id=?
                ''', (mente_id,))
            mente_data = self.cursor.fetchone()
            if mente_data:
                ficha_data["mente"] = {
                    "ideais": mente_data[1]
                }
        return ficha_data
    
    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()
            
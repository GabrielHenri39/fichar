import unittest
from fichar import FichaDragonAge



class TesteFichaDragonAge(unittest.TestCase):
    def setUp(self):
        self.ficha = FichaDragonAge("dragon_age.db")
        self.ficha.inserir_personagem("Gandalf", 100, 100, 100, 100, 100, 100, 100, 100, 100)
        self.ficha.inserir_corpo("cabeca", "corpo", "mao1", "mao2", "pernas", "pes")
        self.ficha.inserir_atributos(100, 100, 100, 100, 100)
        self.ficha.inserir_mente("ideais")
        self.ficha.inserir_personagem("Frodo", 100, 100, 100, 100, 100, 100, 100, 100, 100)
        self.ficha.inserir_corpo("cabeca", "corpo", "mao1", "mao2", "pernas", "pes")
        self.ficha.inserir_atributos(100, 100, 100, 100, 100)
        self.ficha.inserir_mente("ideais")
    
    def teste_recuperar_ficha(self):
        ficha_data = self.ficha.recuperar_ficha(1)
        self.assertEqual(ficha_data["personagem"]["nome"], "Gandalf")
        self.assertEqual(ficha_data["corpo"]["cabeca"], "cabeca")
        self.assertEqual(ficha_data["atributos"]["forca"], 100)
        self.assertEqual(ficha_data["mente"]["ideais"], "ideais")
        self.ficha.fechar_conexao()
    def teste_recuperar_ficha_nao_encontrada(self):
        fichar_data = self.ficha.recuperar_ficha(2)
        self.assertIsNone(fichar_data)
        self.ficha.fechar_conexao()
    
    def teste_inserir_personagem(self):
        self.ficha.inserir_personagem("Gandalf", 100, 100, 100, 100, 100, 100, 100, 100, 100)
        self.ficha.fechar_conexao()
        self.ficha = FichaDragonAge("dragon_age.db")
        ficha_data = self.ficha.recuperar_ficha(1)
        self.assertEqual(ficha_data["personagem"]["nome"], "Gandalf")
        self.ficha.fechar_conexao()
    
    def teste_inserir_corpo(self):
        self.ficha.inserir_corpo("cabeca", "corpo", "mao1", "mao2", "pernas", "pes")
        self.ficha.fechar_conexao()
        self.ficha = FichaDragonAge("dragon_age.db")
        ficha_data = self.ficha.recuperar_ficha(1)
        self.assertEqual(ficha_data["corpo"]["cabeca"], "cabeca")
        self.ficha.fechar_conexao()

    def teste_inserir_atributos(self):
        self.ficha.inserir_atributos(100, 100, 100, 100, 100)
        self.ficha.fechar_conexao()
        self.ficha = FichaDragonAge("dragon_age.db")
        ficha_data = self.ficha.recuperar_ficha(1)
        self.assertEqual(ficha_data["atributos"]["forca"], 100)
        self.ficha.fechar_conexao()

    def teste_inserir_mente(self):
        self.ficha.inserir_mente("ideais")
        self.ficha.fechar_conexao()
        self.ficha = FichaDragonAge("dragon_age.db")
        ficha_data = self.ficha.recuperar_ficha(1)
        self.assertEqual(ficha_data["mente"]["ideais"], "ideais")
        self.ficha.fechar_conexao()


if __name__ == '__main__':
    unittest.main()
    
    

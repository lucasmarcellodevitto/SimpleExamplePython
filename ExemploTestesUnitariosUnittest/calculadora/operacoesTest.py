import unittest
from operacoes import Operacoes

class OperacoesTest(unittest.TestCase):
    
     operacoes  = Operacoes(10, 2)

     def test_operacoes_soma(self):
         self.assertEqual(self.operacoes.soma(), 12)
    
     def test_operacoes_subtrai(self):
         self.assertEqual(self.operacoes.subtrai(), 8)
    
     def test_operacoes_multiplica(self):
         self.assertEqual(self.operacoes.multiplica(), 20)
    
     def test_operacoes_divide(self):
         self.assertEqual(self.operacoes.divide(), 5)
         
if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
import unittest
import calculadora_riesgo_financiero as crf


class AllTesting(unittest.TestCase):
    
    def setUp(self):
        self.perfil_base = {"Nombre":"Alan", "Apellido":"Smithee", "Edad":10, "Salario Mensual":100, "Deuda":50, "Riesgo":"NA"}
        
    def test_creation(self):
        self.assertEqual(crf.crear_perfil("Alan", "Smithee",10,100,50), self.perfil_base)

    def test_failure(self):
        self.assertEqual(1,1)

        
if __name__ == '__main__':
    unittest.main()

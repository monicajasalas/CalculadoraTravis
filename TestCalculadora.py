import unittest

from calculadora import Calculadora

class CalculadoraTest(unittest.TestCase):
	
	def setUp(self):
		self.calc = Calculadora()
	

	def test_valor_de_inicio_igual_a_cero(self):
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def test_sumar_2_mas_2_igual_4(self):
		self.calc.suma(2,2)
		self.assertEquals(self.calc.obtener_resultado(),4)


	def test_suma_negativos_numero(self):
		self.calc.suma(-2, 2)
		self.assertEquals(self.calc.obtener_resultado(),0)

	def test_suma_letras_numero(self):
		self.calc.suma('w', 3)
		self.assertEqual(self.calc.obtener_resultado(),0)


	def test_resta_dos_numeros(self):
		self.calc.resta(6,2)	
		self.assertEquals(self.calc.obtener_resultado(),4)

	def test_resta_negativa(self):
		self.calc.resta(-32,12)
		self.assertEquals(self.calc.obtener_resultado(),-44)

	def test_resta_numer_negativa(self):
		self.calc.resta(3,21)
		self.assertEquals(self.calc.obtener_resultado(),-18)

	def test_resta_letras_numero(self):
		self.calc.suma(3,'eew')
		self.assertEqual(self.calc.obtener_resultado(),0)
	
	def test_multiplicacion_dos_numeros(self):
		self.calc.multiplicacion(12,4)
		self.assertEquals(self.calc.obtener_resultado(),48)

	def test_multiplicacion_letras_numero(self):
		self.calc.multiplicacion('w',3)
		self.assertEqual(self.calc.obtener_resultado(),0)

	def test_division_dos_numeros(self):
		self.calc.division(21,7)
		self.assertEquals(self.calc.obtener_resultado(),3)

	def test_division_entre_cero(self):
		self.calc.division(32,0)
		self.assertEquals(self.calc.obtener_resultado(),0)

	def test_division_entre_ceroC(self):
		self.calc.division(0,32)
		self.assertEquals(self.calc.obtener_resultado(),0)

	def test_division_letras_numero(self):
		self.calc.division('log',3)
		self.assertEqual(self.calc.obtener_resultado(),0)

	def test_potencia_dos_numero(self):
		self.calc.potencia(3,4)
		self.assertEquals(self.calc.obtener_resultado(),81)

	def test_potencia_dos_numeroC(self):
		self.calc.potencia(2,0)
		self.assertEquals(self.calc.obtener_resultado(),1)

	def test_potencia_dos_numeros_cero(self):
		self.calc.potencia(0,2)
		self.assertEquals(self.calc.obtener_resultado(),0)

	def test_potencia_numero_letra(self):
		self.calc.potencia('T', 6)
		self.assertEquals(self.calc.obtener_resultado(),0)

	def test_potencia_neg(self):
		self.calc.potencia(-2,2)
		self.assertEquals(self.calc.obtener_resultado(),4)

	def test_potencia_letras_numero(self):
		self.calc.potencia(4,'#')
		self.assertEquals(self.calc.obtener_resultado(),0)

	def test_raiz_ene(self):
		self.calc.raiz(2,2)
		self.assertEquals(self.calc.obtener_resultado(),1.4)

	def test_raiz_neg(self):
		self.calc.raiz(-4, 2)
		self.assertEquals(self.calc.obtener_resultado(), 0)

	def test_raiz_numero_letra(self):
		self.calc.raiz('T', 6)
		self.assertEquals(self.calc.obtener_resultado(),0)

	def test_raiz_numero_uno(self):
		self.calc.raiz(27,3)
		self.assertEquals(self.calc.obtener_resultado(),3)
	

if __name__ == '__main__':
	unittest.main()

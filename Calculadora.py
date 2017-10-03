class Calculadora():

    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def suma(self, num1, num2):
        try:
            self.resultado = int(num1) +int(num2)
        except ValueError:
            print "Solo numeros enteros"

    def resta(self, num1, num2):
        try:
            self.resultado = int(num1) - int(num2)
        except ValueError:
            print "Solo numeros enteros"

    def multiplicacion(self, num1, num2):
        try:
            self.resultado = int(num1) * int(num2)
        except ValueError:
            print "Solo numeros enteros"

    def division(self, num1, num2):
        try:
            if num1 > 0 and num2 > 0:
                self.resultado = int(num1) / int(num2)
            else:
                print "No se aceptan ceros"
        except ValueError:
            print "Solo numeros enteros"

    def potencia(self, num1, num2):
        try:
            self.resultado = int(num1) ** int(num2)
        except ValueError:
            print "Solo numeros enteros"

    def raiz(self, num1, num2):
        try:
            if int(num1) < 0 or int(num2) < 0:
                print "Error"
            else:
                self.resultado = round(num1**(1.0 / num2), 1)
        except ValueError:
            print "Solo numeros enteros"

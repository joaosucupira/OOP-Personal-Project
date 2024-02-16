import math

class Retangulo:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        area = self.width * self.height
        return area
    
    def perimetro(self):
        perimetro = self.width * 2 + self.height * 2
        return perimetro
    
    def diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** (1/2)
        return diagonal
    
class Quadrado:
    def __init__(self, width):
        self.width = width
        
    def area(self):
        area = self.width ** 2
        return area
    
    def perimetro(self):
        perimetro = self.width * 4
        return perimetro
    
class Circulo:
    def __init__(self, raio):
        self.raio = raio
        
    def area(self):
        area = self.raio ** 2 * math.pi
        return area
    
    def circunferencia(self):
        circunferencia = 2 * math.pi * self.raio
        return circunferencia
    


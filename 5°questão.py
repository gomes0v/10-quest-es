base = int(input("Digite a medida da base: "))
altura = int(input("Digite a medida da altura: "))
area = base * altura/2
lado1 = int(input("Digite a medida do primeiro lado: "))
lado2 = int(input("Digite a medida do segundo lado: "))
lado3 = int(input("Digite a medida do terceiro lado: "))
perimetro = lado1 + lado2 + lado3
class Triângulo:
    def __init__ (self, area, perimetro ):
        self.area = area
        self.perimetro = perimetro
    def area(self):
        return f"a área do triângulo é = {self.area} "
    def perimetro(self):
        return f"O perímetro do triângulo é = {self.perimetro} "
if __name__ == "__main__":
    triangulo1 = Triângulo("10", "16", "9")
print(triangulo1.area())
print(triangulo1.perimetro())
    

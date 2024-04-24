class Carro:
    def __init__ (self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 
        self.cor = cor 
    def ligar(self):
        return f"{self.modelo} o carro tá ligado"
    def desligar(self):
        return f"{self.modelo} o carro está desligado"
    def acelerar(self):
        return f"{self.modelo} o carro está acelerando. Vru vru vru"
if __name__ == "__main__":
    carro1 = Carro("Ford", "Fiesta", "2015", "Branco")
print(carro1.ligar())
print(carro1.desligar())
print(carro1.acelerar())

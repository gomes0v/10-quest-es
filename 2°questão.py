class Animal:
    def __init__ (self, nome, idade, espécie):
        self.nome = nome
        self.idade = idade
        self.espécie = espécie
    def som(self):
        return f"O {self.nome} está rugindo, Huar huar huar"
    def informação_do_animal(self):
        return f"O {self.nome} é o rei da savana e é um animal incrivelmente formidável"
if __name__  == "__main__":
    animal1 = Animal("Leão", "15 anos", "Panthera")
print(animal1.som())
print(animal1.informação_do_animal())
class Animal:
    nome = str()
    idade = int()

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Pessoa(Animal):
    def maioridade(self):
        if self.idade < 18:
            print(f"{self.nome} é menor de idade.")
        elif self.idade < 21:
            print(f"{self.nome} é maior de idade no Brasil, e menor no USA.")
        elif self.idade >= 21:
            print(f"{self.nome} é maior de idade")

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca


felipe = Pessoa(nome="Felipe", idade=18)
fernando = Pessoa(nome="Fernando", idade=24)
gustavo = Pessoa(nome="Gustavo", idade=25)
dinho = Cachorro(nome="Dinho", idade=15, raca="Shnawzer")

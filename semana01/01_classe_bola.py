""" 
Classe Bola: Crie uma classe que modele uma bola:
        Atributos: Cor, circunferência, material
        Métodos: trocaCor e mostraCor
"""

class Bola:
    def __init__(self,cor,circunferencia,material):
        self.__cor = cor
        self.__circunferencia = circunferencia
        self.__material = material

    def trocarCor(self,novaCor):
        self.__cor = novaCor
    
    def mostrarCor(self):
        return self.__cor


bola = Bola("azul","20","coro")

print(bola.mostrarCor())
bola.trocarCor("verde")
print(bola.mostrarCor())
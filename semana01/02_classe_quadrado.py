"""
Classe Quadrado: Crie uma classe que modele um quadrado:
    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""
class Quadrado:
    def __init__(self, tamanho_lado):
        self.__tamanho_lado = tamanho_lado
    
    def mudarValorLado(self, novo_lado):
        self.__tamanho_lado = novo_lado
    
    def calcArea(self):
        return self.__tamanho_lado**2 
    
    def mostraValor(self):
        return self.__tamanho_lado

quadrado = Quadrado(10)
print(quadrado.mostraValor())

quadrado.mudarValorLado(5)
print(quadrado.mostraValor())

print(quadrado.calcArea())
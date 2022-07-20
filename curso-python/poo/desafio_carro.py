#!/usr/bin/python3
class Carro:
    def __init__(self, velocidade_max):
        self.velocidade_max = velocidade_max
        self.velocidade = 0

    def acelerar(self, delta=5):
        self.velocidade += delta

        if self.velocidade > self.velocidade_max:
            self.velocidade = self.velocidade_max
        
        return self.velocidade

    def frear(self, delta=5):
        self.velocidade -= delta
        
        if self.velocidade < 0:
            self.velocidade = 0
        
        return self.velocidade


if __name__ == "__main__":
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))

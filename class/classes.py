from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self) -> None:
      pass
    
    @abstractmethod
    def ligar(self):
        pass
        
    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
      pass
    
    def ligar(self):
        print("ligando...")
    
    def desligar(self):
      print("desligando...")
        
carro_ford = Carro()
carro_ford.ligar()
carro_ford.desligar()
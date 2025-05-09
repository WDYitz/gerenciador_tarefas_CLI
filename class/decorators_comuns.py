# @classmethod
# @staticmethod

class MyClass:
    value = 10 # Atributo classe
    def __init__(self, name) -> None:
        self.name = name # Atributo de instância
    
    def instance_method(self):
        return f"Instância: {self.name}"
    
    @classmethod   
    def class_method(cls):
        return f"Classe: {cls.value}"
      
    @staticmethod
    def static_method():
        return "Método estático chamado"
    
obj = MyClass("Exemplo")
obj.name

class Carro:
    def __init__(self, modelo, ano) -> None:
        self.modelo = modelo
        self.ano = ano
    
    @classmethod
    def create_car(cls, config):
      modelo, ano = config.split(",")
      return cls(modelo, int(ano))
      

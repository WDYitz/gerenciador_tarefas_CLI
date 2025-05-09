from typing import Any

def my_decorator(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("Depois da função ser chamada")
    return wrapper
  
@my_decorator
def say_hello():
    print("Olá!")
    
say_hello()

class ClassDecorator:
    def __init__(self, func) -> None:
        self.func = func
    
    def __call__(self) -> Any:
        print("Antes da função ser chamada")
        self.func()
        print("Depois da função ser chamada")

@ClassDecorator
def second_function():
    print("Olá da segunda função!")
    
second_function()
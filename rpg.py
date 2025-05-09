# Character class 
# Hero class
# Monster class

class Character:
    def __init__(self, name, life, level) -> None:
      self.__name = name
      self.__life = life
      self.__level = level
    
    def get_name(self):
      return self.__name
    
    def get_life(self):
      return self.__life
    
    def get_level(self):
      return self.__level
    
    def get_details(self):
      return f"Name: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}"
    
    def receive_attack(self, damage):
      self.__life -= damage
      if self.__life < 0:
        self.__life = 0
      
    def attack(self, target, _damage):
      damage = self.__level * 1.5 + _damage
      target.receive_attack(damage)
      print(f"{self.get_name()} attacked {target.get_name()} and dealt a total of {damage} damage!\n") 
    

class Hero(Character):
    def __init__(self, name, life, level, hability) -> None:
      super().__init__(name, life, level)
      self.__hability = hability
    
    def get_hability(self):
      return self.__hability
    
    def get_details(self):
      return f"{super().get_details()}\nAttack Type: {self.get_hability()}\n"
       

class Monster(Character):
    def __init__(self, name, life, level, type) -> None:
      super().__init__(name, life, level)
      self.__type = type
    
    def get_type(self):
      return self.__type
    
    def get_details(self):
      return f"{super().get_details()}\nType: {self.get_type()}\n"
    
class Game:
    def __init__(self, hero, monster) -> None:
      self.hero = hero
      self.monster = monster
    
    def start_battle(self):
      print("Starting battle!")
      print(f"{self.hero.get_details()}")
      print(f"{self.monster.get_details()}")
            
      # Simulate battle
      while self.hero.get_life() > 0 and self.monster.get_life() > 0:
        input("Press Enter to attack! 🎯")
        attack_choice = input("Choose your attack (1: Primary, 2: Special): ")
        if attack_choice == "1":
          damage = 10
          print(f"\n{self.hero.get_name()} attacks {self.monster.get_name()} with Primary Attack!")
          self.hero.attack(self.monster, damage)
        elif attack_choice == "2":
          damage = 20
          print(f"\n{self.hero.get_name()} attacks {self.monster.get_name()} with Special Attack!")
          self.hero.attack(self.monster, damage)
        else:
          print("Invalid choice! Try again.")
          continue
        
        if self.monster.get_life() > 0:
          print(f"\n{self.monster.get_name()} attacks back!")
          self.monster.attack(self.hero, 10)
        
        if self.hero.get_life() > 0 and self.monster.get_life() <= 0:
          print("\nCongratulations! You defeated the monster!")
        elif self.hero.get_life() <= 0 and self.monster.get_life() > 0:
          print("\nGame Over! You have been defeated.")

hero = Hero("Hero", 100, 1, "Sword Slash")
monster = Monster("Goblin", 120, 5, "Beast") 

game = Game(hero, monster)
game.start_battle()
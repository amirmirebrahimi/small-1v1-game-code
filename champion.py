from abc import ABC, abstractmethod

class Champion(ABC):
    def __init__(self, Health, Damage, Speed , Range,Location):
        self.Health = Health
        self.Damage = Damage
        self.speed = Speed
        self.Range = Range
        self.Location = Location

    def attack(self , enemy):
        distance = abs(self.Location - enemy.Location)
        if distance <= self.Range:
           enemy.Health -= self.Daamage



    def move(self , dir):
           if dir == 1:
            self.Location += self.Speed

           elif dir == -1:
            self.Location -= self.Speed

    @abstractmethod

    def Special_ability(self,enemy):
        pass
    

    @classmethod
    @abstractmethod
    def create_default(cls):
        pass

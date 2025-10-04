from abc import ABC, abstractmethod

class Champion(ABC):
    def __init__(self, Health, Damage, Speed):
        self.health = Health
        self.damage = Damage
        self.speed = Speed

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def move(self):
        pass


    @abstractmethod
    def get_dammaged(self):
        pass
    

    @classmethod
    @abstractmethod
    def create_default(cls):
        pass

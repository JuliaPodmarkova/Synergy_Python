# Задача 1. Оркестр животных и их симфония методов

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    @abstractmethod
    def make_sound(self):
        return self.sound

class Mammal(Animal):
    def __init__(self, name, sound, num_legs):
        super().__init__(name, sound)
        self.num_legs = num_legs

    def make_sound(self):
        return self.sound

    def give_birth(self):
        return f'{self.name} получил потомство'

class Bird(Animal):
    def __init__(self, name, sound, can_fly):
        super().__init__(name, sound)
        self.can_fly = can_fly

    def make_sound(self):
        return self.sound

    def fly(self):
        return f'{self.name} летит'

bird1 = Bird('Воробей', 'Чирик-чирик!', True)
bird2 = Bird('Ворона', 'Кар-кар!', True)

print(f'{bird1.name} говорит {bird1.make_sound()} и {bird1.fly()}')
print(f'{bird2.name} говорит {bird2.make_sound()} и {bird2.fly()}')

mammal1 = Mammal('Лев', 'Аррррр!', 4)
mammal2 = Mammal('Волк', 'Ууууууу!', 4)

print(f'{mammal1.name} бегает на {mammal1.num_legs} лапах, рычит {mammal1.make_sound()}')
print(f'Когда {mammal1.name} находит пару, тогда {mammal1.give_birth()}')

print(f'{mammal2.name} бегает на {mammal2.num_legs} лапах, рычит {mammal2.make_sound()}')
print(f'Когда {mammal2.name} находит пару, тогда {mammal2.give_birth()}')

# Parent Class
class Animal:

    def __init__(self, spec):
        self.species = spec

    def whatAnimal(self):
        print(self.species)

#Child Class
class Cat(Animal):

    def __init__(self, spec, snd):
        super().__init__(spec)
        self.sound = snd

    def meow(self):
        print(self.species, self.sound)

#Child Class
class Dog(Animal):

    def __init__(self, spec, snd):
        super().__init__(spec)
        self.sound = snd

    def bark(self):
        print(self.species, self.sound)

animal = Animal('Hamster')
milo = Cat('British Short Hair', 'Meow!')
roger = Dog('German Shepherd', 'Woof!')

animal.whatAnimal()
milo.meow()
roger.bark()
#Creating Parent Class
class Person:
    #Instance Attributes
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    #Methods
    def printname(self):
        print(self.firstname, self.lastname)

#Child Class 1
class Idol(Person):
    #Attributes
    def __init__(self, fname, lname, gr):
        super().__init__(fname, lname)
        self.group = gr

    #Methods
    def introduction(self):
        print("Hello, I'm", self.firstname, self.lastname, "from", self.group)

#Child Class 2
class Manager(Person):
    #Attributes
    def __init__(self, fname, lname, lab):
        super().__init__(fname, lname)
        self.label = lab

    #Methods
    def info(self):
        print(self.firstname, self.lastname, "Manager of Idols in", self.label)

#Creating Object
orang = Person("Ahmad", "Faiz")
idol1 = Idol("Shin", "Ryu-jin", "ITZY")
idol2 = Idol("Myoui", "Mina", "TWICE")
idol3 = Idol("Kim", "Ji-soo", "Blackpink")
manager1 = Manager("Park", "Jin-young","JYP Entertainment")
manager2 = Manager("Lee", "Soo-man", "SM Entertainment")

#Calling InstanceMethods
orang.printname()
idol1.introduction()
idol2.introduction()
idol3.introduction()
manager1.info()
manager2.info()

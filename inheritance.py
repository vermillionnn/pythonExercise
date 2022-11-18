class Person:
    #attributes
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    #method
    def printname(self):
        print(self.firstname, self.lastname)

#Menggunakan class Person untuk membuat objek lalu mengeksekusi method printname()
orang = Person("Shin", "Ryujin")
orang.printname()

#Membuat Child Class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

murid = Student("Hwang", "Yeji", 2023)
murid.printname()
murid.welcome()


from abc import *

class Animal(ABC):
    def __init__(self, name, age, gender):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def __repr__(self):
        pass    

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__}"
    
    def make_sound(self):
        return "Woof!" 
    
class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__}"
    
    def make_sound(self):
        return "Meow meow!"

class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender= "Female")

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__}"
    
    def make_sound(self):
        return "Meow"
    
class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender= "Male")

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__}"
    
    def make_sound(self):
        return "Hiss"
    
a = Tomcat("Tom", 2)
b = Dog("joss", 2, "male")

print(repr(a))
print(b.make_sound())
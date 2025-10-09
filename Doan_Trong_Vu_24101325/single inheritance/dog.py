from animal import Animal
class Dog(Animal):
    def __init__(self, eat, bark):
        self.eat = eat
        self.bark = bark
        return 'barking'
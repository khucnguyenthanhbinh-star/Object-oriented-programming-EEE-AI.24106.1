from animal import Mammal
from food import Vegetable, Fruit, Meat

class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, (Vegetable, Fruit)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"Mouse [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"Dog [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, (Vegetable, Meat)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.30 * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"Cat [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 1.00 * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self):
        return f"Tiger [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

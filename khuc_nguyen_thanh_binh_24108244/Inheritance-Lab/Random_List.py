import random

class RandomList(list):
    def get_random_element(self):
        if not self:
            raise IndexError("Cannot get random element from an empty list")
        index = random.randint(0, len(self) - 1)
        return self.pop(index)
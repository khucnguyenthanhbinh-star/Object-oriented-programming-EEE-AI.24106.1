import random

class RandomList(list):
    def get_random_element(self):
        if self:
            random_element = random.choice(self)
            self.remove(random_element)
            return random_element
        else:
            return None


print(type(RandomList))
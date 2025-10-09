import random
class RandomList(list):
    def get_random_element(self):
        if not self:
            return None
        element = random.choice(self)
        self.remove(element)
        return element
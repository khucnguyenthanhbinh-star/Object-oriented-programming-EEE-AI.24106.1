import random
class RandomList(list):
    def get_random_element():
        if not self:
            return None
        index = random.randrange(len(self))
        return self.pop(index)
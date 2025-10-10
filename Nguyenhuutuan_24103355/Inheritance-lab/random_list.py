import random
class RandomList(list):
    def get_random_element(self):
        if len(self) == 0:
            return None
        index = random.randint(0, len(self) - 1)
        return self.pop(index)
class RandomList:
    def get_random_element(self):
        if not self:
            return None
        index = random.randrange(len(self))
        return self.pop(index)




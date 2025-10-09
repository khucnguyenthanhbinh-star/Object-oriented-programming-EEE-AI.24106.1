import random 
random.seed(43)
class RandomList(list):
    def  get_random_element(self):
        index = random.randrange(len(self))
        element = self.pop(index)
        return element

my_list = []
for i in range(0, 10):
    my_list.append(random.randint(1, 10))
print(my_list)

ls = RandomList(my_list)
print(ls.get_random_element())
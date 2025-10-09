import random

class RandomList(list):
      def get_random_element(self):
            index = random.randrange(len(self))
            return self.pop(index)
      
my_list = []
for i in range(0, 10):
      my_list.append(random.randrange(1, 10))

ran = RandomList(my_list)

print(my_list)
print(ran.get_random_element())

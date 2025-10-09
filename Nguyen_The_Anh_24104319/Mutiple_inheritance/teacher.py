from Employee import employee
from Person import person 
class Teacher(person,employee):
    def teach(self):
        return "teaching"
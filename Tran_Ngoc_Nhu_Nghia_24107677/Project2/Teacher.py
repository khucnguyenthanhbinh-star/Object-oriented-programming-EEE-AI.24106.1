from Person import Person
from Employee  import Employee

class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."

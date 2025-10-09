from person import Person 
from employee import Employee

class Teacher(Person, Employee):
    def teacher(self):
        return "teaching..."
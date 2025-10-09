from .person import Person
from .employee import Employee
class Teacher(Person, Emloyee):
	def teach(self):
		return"teaching..." 
class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return f"Person(name='{self.name}', surname='{self.surname}')"

    def __eq__(self, other):
        if isinstance(other, Person):
            return (self.name == other.name and self.surname == other.surname)
        return False


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __str__(self):
        return f"Group: {self.name}, People: " + ", ".join(str(person) for person in self.people)

    def __repr__(self):
        return f"Group(name='{self.name}', people={self.people})"

    def __contains__(self, person):
        return person in self.people

p0 = Person('Aliko', 'Dangote') 
p1 = Person('Bill', 'Gates') 
p2 = Person('Warren', 'Buffet') 
p3 = Person('Elon', 'Musk') 
p4 = p2 + p3 
 
first_group = Group('__VIP__', [p0, p1, p2]) 
second_group = Group('Special', [p3, p4]) 
third_group = first_group + second_group

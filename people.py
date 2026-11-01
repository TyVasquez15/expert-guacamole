# people.py

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class Faculty(Person):
    def __init__(self, firstname, lastname, department):
        super().__init__(firstname, lastname)
        self.department = department


class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

    def set_class(self, classyear):
        self.classyear = classyear

    def set_major(self, major):
        self.major = major

    def set_advisor(self, advisor):
        self.advisor = advisor

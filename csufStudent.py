# Person and CSUF_Student Class

class MyTypeError(Exception):
    pass


class Person:
    def __init__(self, first_name, last_name, gender, age):
        if not age.isnumeric():
            raise MyTypeError("Age must be in only numeric numbers.")

        if gender not in ["Male", "Female", "Non-Binary"]:
            raise MyTypeError("Gender must be Male, Female, or Non-Binary.")

        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.first_name + " " + self.last_name

class CSUF_Student(Person):
 
    school = "California State University, Fullerton"
    student_count = 0

    def __init__(self, first_name, last_name, gender, age, ID, major):
        super().__init__(first_name, last_name, gender, age)

        self.__ID = ID
        self.major = major

        CSUF_Student.student_count += 1

    def getID(self):
        return self.__ID

    def ChangeMajor(self, new_major):
        self.major = new_major

    def getName(self):
        return super().getName() + " (ID: " + self.__ID + ")"
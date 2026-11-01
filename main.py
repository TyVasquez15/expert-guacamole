from people import Faculty, Student

faculty = []
students = []


def add_faculty():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    department = input("Enter department: ")

    new_faculty = Faculty(firstname, lastname, department)
    faculty.append(new_faculty)


def print_faculty():
    print("======================= FACULTY =======================")
    print(f'{"Record":8}{"Name":20}{"Department":25}')
    print(f'{"======":8}{"====================":20}{"=========================":25}')

    for i in range(len(faculty)):
        name = faculty[i].firstname + " " + faculty[i].lastname
        print(f"{i:<8}{name:20}{faculty[i].department:25}")


def add_student():
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")
    classyear = input("Enter class year: ")
    major = input("Enter major: ")

    print_faculty()
    advisor_number = int(input("Enter faculty advisor: "))

    if advisor_number >= 0 and advisor_number < len(faculty):
        new_student = Student(firstname, lastname)

        new_student.set_class(classyear)
        new_student.set_major(major)
        new_student.set_advisor(faculty[advisor_number])

        students.append(new_student)
    else:
        print("Invalid faculty record number.")


def print_students():
    print("===================================== STUDENTS ======================================")
    print(f'{"Name":20}{"Class":10}{"Major":26}{"Advisor":25}')
    print(f'{"====================":20}{"========":10}{"=========================":26}{"=========================":25}')

    for student in students:
        name = student.firstname + " " + student.lastname
        advisor = student.advisor.firstname + " " + student.advisor.lastname

        print(f"{name:20}{student.classyear:10}{student.major:26}{advisor:25}")


while True:
    print("\n *** TUFFY TITAN STUDENT/FACULTY MAIN MENU")
    print("1. Add faculty")
    print("2. Print faculty")
    print("3. Add student")
    print("4. Print student")
    print("9. Exit the program")

    choice = input("Enter menu choice: ")

    if choice == "1":
        add_faculty()

    elif choice == "2":
        print_faculty()

    elif choice == "3":
        if len(faculty) > 0:
            add_student()
        else:
            print("Add faculty first.")

    elif choice == "4":
        print_students()

    elif choice == "9":
        break

    else:
        print("Invalid choice.")

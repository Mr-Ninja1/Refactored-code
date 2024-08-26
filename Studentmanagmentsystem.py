#class holds student infomation
class StudentInfo:
    def __init__(self, id, name, age, major):
        self.id = id
        self.name = name
        self.age = age
        self.major = major

class StudentUpdater:
    def __init__(self, student):
        self.student = student

    def update_student(self, name=None, age=None, major=None):
        update_student_attributes(self.student, name, age, major)

class StudentDisplay:
    def __init__(self, student):
        self.student = student

    def display_student(self):
        print(format_student(self.student))

def update_student_attributes(student, name=None, age=None, major=None):
    if name:
        student.name = name
    if age:
        student.age = age
    if major:
        student.major = major

def format_student(student):
    return f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Major: {student.major}"

from abc import ABC, abstractmethod

class IStudentRepository(ABC):
    def __init__(self):
        self.students = None

    @abstractmethod
    def add_student(self, student):
        pass

    @abstractmethod
    def remove_student(self, student_id):
        pass

    @abstractmethod
    def display_all_students(self):
        pass

    @abstractmethod
    def get_student_by_id(self, student_id):
        pass  #  method to retrieve a student by ID

class StudentDatabase(IStudentRepository):
    def __init__(self):
        super().__init__()
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                break

    def display_all_students(self):
        for student in self.students:
            display = StudentDisplay(student)
            display.display_student()

    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

class StudentManagementSystem:
    def __init__(self, repository: IStudentRepository):
        self.database = repository
        self.updater = StudentUpdater(None)

    def add_new_student(self, id, name, age, major):
        student = StudentInfo(id, name, age, major)
        self.database.add_student(student)

    def delete_student(self, student_id):
        self.database.remove_student(student_id)

    def update_student_info(self, student_id, name=None, age=None, major=None):
        student = self.database.get_student_by_id(student_id)
        if student:
            self.updater.student = student
            self.updater.update_student(name, age, major)
            print("Student details updated.")
        else:
            print(f"Student with ID {student_id} not found.")

    def view_student(self, student_id):
        student = self.database.get_student_by_id(student_id)
        if student:
            display = StudentDisplay(student)
            display.display_student()
        else:
            print(f"Student with ID {student_id} not found.")

    def show_all_students(self):
        self.database.display_all_students()
# This method is called first when the program runs and it displays the programs options menu
    #Added the menu to improve user interaction
    def display_menu(self):
        while True:
            print("\nStudent Management System Menu:")
            print("1. Add new student")
            print("2. view student details by ID")
            print("3. Update student information")
            print("4. Display all students")
            print("5. Delete student from system")
            print("6. Exit")
            choice = input("Enter your choice (1/2/3/4/5): ")
            print('---------------------------------------------------------------') # nothing serious just creats a line that separates the menu from the output
            if choice == "1":
                id = int(input("Enter student ID: "))
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                major = input("Enter student major: ")
                sys.add_new_student(id, name, age, major)
            elif choice == "2":
                student_id = int(input("Enter student ID to view: "))
                self.view_student(student_id)
            elif choice == "3":
                student_id = int(input("Enter student ID to update: "))
                name = input("Enter updated student name (leave blank to keep current): ")
                age = input("Enter updated student age (leave blank to keep current): ")
                major = input("Enter updated student major (leave blank to keep current): ")
                self.update_student_info(student_id, name, age, major)
            elif choice=="4":
                self.show_all_students()
            elif choice=="5":
                student_id = int(input("Enter student ID to delete: "))
                self.delete_student(student_id)
            elif choice== "6":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    database_instance = StudentDatabase()
    sys = StudentManagementSystem(repository=database_instance)
    sys.display_menu()

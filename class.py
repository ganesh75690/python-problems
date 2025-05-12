# Simple class program in Python      
class Person:       
    def __init__(self, name, age):     
        self.name = name         
        self.age = age      

    def greet(self):     
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class
person1 = Person("John", 25)

# Call the greet method
person1.greet()

# College Management System

class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")


class College:
    def __init__(self, college_name):
        self.college_name = college_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} has been added to {self.college_name}.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student {student.name} has been removed from {self.college_name}.")
                return
        print(f"Student with ID {student_id} not found.")

    def display_all_students(self):
        if not self.students:
            print(f"No students are currently enrolled in {self.college_name}.")
        else:
            print(f"Students enrolled in {self.college_name}:")
            for student in self.students:
                print(f"- {student.name} (ID: {student.student_id})")


# Main Program
college = College("ABC College")

# Adding students
student1 = Student(101, "Alice", 20, "Computer Science")
student2 = Student(102, "Bob", 22, "Mechanical Engineering")
student3 = Student(103, "Charlie", 19, "Electrical Engineering")

college.add_student(student1)
college.add_student(student2)
college.add_student(student3)

# Display all students
college.display_all_students()

# Display details of a specific student
print("\nDetails of a specific student:")
student1.display_details()

# Remove a student
college.remove_student(102)

# Display all students after removal
college.display_all_students()     
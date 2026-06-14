# Develop a simple OOP-based python class Student with attributes like name, roll number,and marks.Implement methods to input and display details.
class Student:
    def setData(self):
        self.name = " "
        self.roll_no = " "
        self.marks = 0

    def inputDetails(self):
        self.name=input("Input Student Name:")
        self.roll_no=input("Input Roll Number: ")
        self.marks=int(input("Input Marks: "))

    def displayDetails(self):
        print("Students Details..")
        print("Name: ", self.name)
        print("Roll Number: ", self.roll_no)
        print("Marks:" , self.marks)

student1=Student()
student1.inputDetails()
student1.displayDetails()

print("Suhana Paudel")


# Create a program that takes a list of students name and stores them in a file.Then read the file and display the contents.

students=[]
n=int(input("Input Number Of Students: "))

for i in range(n):
    name=input(f"Input Student's Name: ")
    students.append(name)

with open("students.txt","w") as file:
    for student in students:
        file.write(student + "\n")
print("Name Saved Succcessfully\n")

with open("students.txt","r") as file:
    content=file.read()

print("List of Students: ")
print(content)
# 
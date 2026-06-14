students={}
while True:
    print("Students Details..\n")

    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")

    choice = input("Input your choice: ")

    if choice == "1":
        roll = input("Input roll number: ")

        if roll in students:
            print("Student already exists.")
        else:
            name = input("Input name: ")
            marks = input("Input marks: ")
            contact = input("Input contact number: ")
            
            students[roll] = {
                "name": name,
                "marks": marks,
                "contact": contact
            }

            print("Student added successfully!")

    elif choice == "2":
        roll = input("Input roll number to search: ")

        if roll in students:
            print("Student Found:\n")
            print("Roll:", roll)
            print("Name:", students[roll]["name"])
            print("Marks:", students[roll]["marks"])
            print("Contact:", students[roll]["contact"])
        else:
            print("Student not found..")

    elif choice == "3":
        if not students:
            print("Students record not found")
        else:
            print("All Student Records:\n")
            for roll, info in students.items():
                print("Roll:", roll)
                print("Name:", info["name"])
                print("Marks:", info["marks"])
                print("Contact:", info["contact"])

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
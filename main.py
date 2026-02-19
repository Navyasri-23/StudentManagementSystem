students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students.append([name, marks])
        print("Student added successfully!")

    # Show all students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")
            for s in students:
                print("Name:", s[0], "| Marks:", s[1])

    # Search student
    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        for s in students:
            if s[0] == search_name:
                print("Student found!")
                print("Name:", s[0], "| Marks:", s[1])
                found = True
                break

        if not found:
            print("Student not found.")

    # Exit
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")


students = []


def add_student():
    print("\n--- Add Student ---")

    name = input("Student Name: ")
    roll = int(input("Roll Number: "))
    marks = float(input("Marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("Name:", student["name"])
        print("Roll:", student["roll"])
        print("Marks:", student["marks"])
        print("--------------------")


def calculate_result():
    print("\n--- Student Results ---")

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        marks = student["marks"]

        if marks >= 85:
            result = "A"
        elif marks >= 75:
            result = "B"
        elif marks >= 55:
            result = "C"
        else:
            result = "Fail"

        print("Name:", student["name"])
        print("Roll:", student["roll"])
        print("Marks:", marks)
        print("Result:", result)
        print("--------------------")


def student_count():
    print("\n--- Student Count ---")
    print("Total Students:", len(students))


def main():
    while True:
        print("\n==============================")
        print("   STUDENT PERFORMANCE ANALYZER")
        print("==============================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Result")
        print("4. Student Count")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            calculate_result()

        elif choice == "4":
            student_count()

        elif choice == "5":
            print("Thank you for using Student Analyzer!")
            break

        else:
            print("Invalid choice. Try again.")


main()

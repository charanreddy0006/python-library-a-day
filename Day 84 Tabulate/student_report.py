from tabulate import tabulate


students = []


def add_student():
    name = input("Student Name: ")
    marks = float(input("Marks: "))

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "F"

    students.append([name, marks, grade])
    print("Student added successfully!\n")


def show_report():
    if not students:
        print("\nNo student records found.\n")
        return

    print("\nStudent Report")
    print(tabulate(
        students,
        headers=["Name", "Marks", "Grade"],
        tablefmt="grid"
    ))


def main():
    while True:
        print("\n===== Student Report Generator =====")
        print("1. Add Student")
        print("2. View Report")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_report()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
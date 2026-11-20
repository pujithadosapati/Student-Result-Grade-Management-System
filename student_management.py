# Student Result & Grade Management System
students = {}
subjects = ["Python", "Mathematics", "Physics", "Electronics", "English"]
def calculate_result(marks):
    total = sum(marks.values())
    percentage = total / len(subjects)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade


def add_student():
    roll = input("Enter Roll Number: ").strip()

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    marks = {}

    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter {subject} Marks (0-100): "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    students[roll] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    for roll, details in students.items():
        total, percentage, grade = calculate_result(
            details["marks"]
        )

        print("\n------------------------------")
        print("Roll Number:", roll)
        print("Name:", details["name"])
        print("Marks:", details["marks"])
        print("Total:", total, "/", len(subjects) * 100)
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)
        print("------------------------------")


def search_student():
    roll = input("Enter Roll Number to search: ").strip()

    if roll in students:
        details = students[roll]
        total, percentage, grade = calculate_result(
            details["marks"]
        )

        print("\nStudent Found!")
        print("Name:", details["name"])
        print("Marks:", details["marks"])
        print("Total:", total)
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)
    else:
        print("Student not found!")


def update_student():
    roll = input("Enter Roll Number to update: ").strip()

    if roll not in students:
        print("Student not found!")
        return

    print("Updating marks for:", students[roll]["name"])

    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter new {subject} Marks (0-100): "))

                if 0 <= mark <= 100:
                    students[roll]["marks"][subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    print("Student marks updated successfully!")


def performance_summary():
    if not students:
        print("No records available.")
        return

    percentages = []
    pass_count = 0

    print("\n===== PERFORMANCE SUMMARY =====")

    for roll, details in students.items():
        total, percentage, grade = calculate_result(
            details["marks"]
        )

        percentages.append(percentage)

        if grade != "F":
            pass_count += 1

        print(details["name"], "-", round(percentage, 2), "% -", grade)

    print("\nTotal Students:", len(students))
    print("Passed Students:", pass_count)
    print("Failed Students:", len(students) - pass_count)
    print("Class Average:", round(sum(percentages) / len(percentages), 2), "%")
    print("Highest Percentage:", round(max(percentages), 2), "%")
    print("Lowest Percentage:", round(min(percentages), 2), "%")


def main():
    while True:
        print("\n================================")
        print(" STUDENT RESULT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Performance Summary")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            performance_summary()

        elif choice == "6":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice! Please select 1-6.")
if __name__ == "__main__":
    main()

student_data = []
# subjects_list = []
def add_student():
    print("\nEnter student details:")
    sid = input("Student ID: ")
    name = input("Name: ")
    age = int(input("Age: "))
    grade = input("Grade: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    subjects = input("Subjects (comma-separated): ")
    student_data.append({
        "id": sid,
        "name": name,
        "age": age,
        "grade": grade,
        "dob": dob,
        "subjects": [sub.strip() for sub in subjects.split(",")]
    })
    print("Student added successfully!")

def display_all_student():
    for idx, student in enumerate(student_data, start=1):
        print(f"\n👤 Student #{idx}")
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Grade  : {student['grade']}")
        print(f"DOB    : {student['dob']}")
        print(f"Subjects: {student['subjects']}")

def update_student_data():
    sid = input("Enter Student's ID: ")
    found = False

    for student in student_data:
        if student["id"] == sid:
            print(f"\n Student found: {student['name']}")

            # Get new data
            name = input("Enter new name (press Enter to keep current): ")
            age_input = input("Enter new age (press Enter to keep current): ")
            grade = input("Enter new grade (press Enter to keep current): ")
            dob = input(
                "Enter new DOB (YYYY-MM-DD) (press Enter to keep current): ")
            subjects_input = input(
                "Enter new subjects (comma-separated) (press Enter to keep current): ")

            # Only update if something is entered
            if name:
                student["name"] = name
            if age_input:
                student["age"] = int(age_input)
            if grade:
                student["grade"] = grade
            if dob:
                student["dob"] = dob
            if subjects_input:
                student["subjects"] = [sub.strip()
                                       for sub in subjects_input.split(",")]

            print("Student updated successfully!")
            found = True
            break

    if not found:
        print("No student found with that ID.")

def remove_student():
    sid = input("\nEnter the Student ID to remove: ")
    found = False

    for student in student_data:
        if student["id"] == sid:
            student_data.remove(student)
            print(f"Student with ID {sid} has been removed successfully.")
            found = True
            break

    if not found:
        print("No student found with that ID.")

subs = ["Physics", "Maths", "Chemistry", "Environmental Studies", "Python", "Java", "OOPS", "POPS", "C++", "AI/ML"]

while True:
    print("Welcome to the Student Data Organizer!\n")
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_all_student()
    elif choice == 3:
        update_student_data()
    elif choice == 4:
        remove_student()
    elif choice == 5:
        for sub in subs:
            print(sub)
    elif choice == 6:
        print("Program Exited!!")
        break
    else:
        print("Invalid Inputs!!")
        break
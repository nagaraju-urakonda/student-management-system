import json

students = []

students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    students.append({"roll": roll, "name": name, "branch": branch})
    save_data()
    print("Student added successfully.")
def view_students():
    if not students:
        print("No student records found.")
    else:
        print("Student List:")
        for s in students:
            print(f"Roll: {s['roll']}, Name: {s['name']}, Branch: {s['branch']}")
def search_student():
    roll = input("Enter Roll Number to search: ")
    found = False
    for s in students:
        if s["roll"] == roll:
            print(f"Found: Roll: {s['roll']}, Name: {s['name']}, Branch: {s['branch']}")
            found = True
            break
    if not found:
        print("Student not found.")
def update_student():
    roll = input("Enter Roll Number to update: ")
    for s in students:
        if s["roll"] == roll:
            print(f"Current Name: {s['name']}, Branch: {s['branch']}")
            s["name"] = input("Enter new name: ")
            s["branch"] = input("Enter new branch: ")
            save_data() 
            print("Student updated successfully.")
            return
    print("Student not found.")
def delete_student():
    roll = input("Enter Roll Number to delete: ")
    global students
    students = [s for s in students if s["roll"] != roll]
    save_data()
    print(f"{roll} Student deleted.")
def load_data():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
    except FileNotFoundError:
        students = []

def save_data():
    with open("students.json", "w") as f:
        json.dump(students, f)

def menu():
    load_data()
    while True:
        print("\n🎓 Student Management System Menu")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()







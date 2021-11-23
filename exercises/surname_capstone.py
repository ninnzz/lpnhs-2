# Surname capstone
# Simple student record system

# View of student
# View of student grades
# Add student
# Remove student
# Update student info

class_record = {
    "number_of_students": 0,
    "students": [],
    "teacher_name": "Georgia Talabong"
}

student_template = {
    "name": None,
    "age": None,
    "birthday": None,   # YYYY-MM-DD
    "gender": None,
    "grades": {
        "science": None,
        "english": None,
        "math": None,
        "filipino": None
    }
}

def search_student_by_name(record, name):
    # Constraint
    # Name search should be case insensitive
    student = None # Temp variable para di magerror


    student_print(student)


def update_student_info(record, name):
    student = None
    # Perform a search first

    print("\n\nChoose which info you want to change")
    print("1 - Age")
    print("2 - Birthday")
    print("3 - Gender")
    print("4 - Science grade")
    print("5 - Math grade")
    print("6 - English grade")
    print("7 - Filipino grade")
    inp = int(input("Option: "))

    if 0 < inp < 8:
        print("Invalid option")
        return

    # Perform update here

    student_print(student)

def delete_student(record, name):

    # Perform search

    print(f"Student {name} has been deleted!")

def sort_by_name(record):
    sorted_list = []
    # Sort student here

    print_all(sorted_list)

def sort_by_subject_grade(record, subject):
    sorted_list = []
    # Sort student here

    print_all(sorted_list)

def add_student(record):
    name = input("Student name: ")
    age = int(input("Age: "))
    bday = input("Birthday(YYYY-MM-DD): ")
    gender = input("Gender: ")
    sci_grade = float(input("Grade in science: "))
    eng_grade = float(input("Grade in english: "))
    math_grade = float(input("Grade in math: "))
    fil_grade = float(input("Grade in filipino: "))

    student = {
        "name": name,
        "age": age,
        "birthday": bday,   # YYYY-MM-DD
        "gender": gender,
        "grades": {
            "science": sci_grade,
            "english": eng_grade,
            "math": math_grade,
            "filipino": fil_grade
        }
    }

    record["students"].append(student)
    record["number_of_students"] += 1
    student_print(student)

def student_print(student):

    print("*************************************************")
    print(f"Name: {student['name']} Age: {student['age']}")
    print(f"Gender: {student['gender']} Birthday: {student['birthday']}")
    print("Grades")
    print("Science: ", student["grades"]["science"])
    print("Math: ", student["grades"]["math"])
    print("English: ", student["grades"]["english"])
    print("Filipino: ", student["grades"]["filipino"])
    print("")

def print_all(record):

    if "number_of_students" not in record or record["number_of_students"] == 0:
        return print("No student in the record!")
    for s in record["students"]:
        student_print(s)


while True:

    print("\n\nActions")
    print("1 - View all students")
    print("2 - Search student")
    print("3 - Add a student")
    print("4 - Update student info")
    print("5 - Delete student")
    print("6 - Sort by name")
    print("7 - Sort by grade")
    print("0 - Exit")
    inp = int(input("Please choose an option: "))


    if inp == 0:
        print("Thank you for using our class record!")
        break
    elif inp == 1:
        print_all(class_record)
    elif inp == 2:
        name = input("Name to search: ")
        search_student_by_name(class_record, name)
    elif inp == 3:
        add_student(class_record)
    elif inp == 4:
        name = input("Name to update: ")
        update_student_info(record, name)
    elif inp == 5:
        name = input("Name to update: ")
        delete_student(class_record, name)
    elif inp == 6:
        sort_by_name(class_record)
    elif inp == 7:
        subject = input("Subject: ")
        sort_by_subject_grade(class_record, subject)
    else:
        print("Invalid option! Please select another one.")





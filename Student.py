import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Enter the password:  "),
    database="student_db"
)

cursor = conn.cursor()
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    cls = input("Enter class: ")

    query = "INSERT INTO students (name, age, class) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, cls))
    conn.commit()

    print("Student added successfully")


def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
        

def add_marks():
    student_id = int(input("Student ID: "))
    print("Math(1) Science(2) English(3) Physics(4) Chemistry(5)")
    subject_id = int(input("Subject ID (1-5): "))
    

    if subject_id not in range(1, 6):
        print("Invalid Subject ID. Please enter 1–5")
        return

    marks = int(input("Marks: "))

    query = "INSERT INTO results (student_id, subject_id, marks) VALUES (%s, %s, %s)"
    cursor.execute(query, (student_id, subject_id, marks))
    conn.commit()
    print("Marks added")


def view_full_result():
    query = """
    SELECT students.name, subjects.subject_name, results.marks
    FROM results
    JOIN students ON results.student_id = students.id
    JOIN subjects ON results.subject_id = subjects.id
    """

    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)


def calculate_result():
    student_id = int(input("Enter student ID: "))

    query = "SELECT marks FROM results WHERE student_id = %s"
    cursor.execute(query, (student_id,))

    marks = [i[0] for i in cursor.fetchall()]
    

    if not marks:
        print("No marks found")
        return

    total = sum(marks)
    avg = total / len(marks)

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "F"

    status = "Pass" if avg >= 50 else "Fail"

    print("Total:", total)
    print("Average:", avg)
    print("Grade:", grade)
    print("Status:", status)

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Add Marks")
    print("4. View Full Result")
    print("5. Calculate Result")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        add_marks()
    elif choice == "4":
        view_full_result()
    elif choice == "5":
        calculate_result()
    elif choice == "6":
        break
    else:
        print("Invalid choice")

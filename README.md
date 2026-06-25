# 🎓 Student Result Management System

A command-line based Student Result Management System developed using Python, MySQL, and Object-Oriented Programming (OOP). The application helps manage student records, subject results, grades, and pass/fail status through a simple and interactive CLI interface.

---

## 📖 Table of Contents

* Overview
* Features
* Technologies Used
* System Workflow
* Project Structure
* Database Design
* Installation & Setup
* Sample Operations
* Future Improvements

---

## 🚀 Overview

The Student Result Management System is designed to store and manage student academic records efficiently. Users can add, update, delete, and view student information while automatically calculating grades and pass/fail status based on marks obtained.

The project demonstrates practical usage of:

* Python Programming
* Object-Oriented Programming (OOP)
* MySQL Database Management
* SQL JOIN Queries
* CRUD Operations

---

## ✨ Features

### 👨‍🎓 Student Management

* Add new student records
* Update existing student details
* Delete student records
* View all students

### 📚 Result Management

* Add subject-wise marks
* Update student results
* View student performance reports

### 🏆 Grade Calculation

* Automatic grade assignment based on marks
* Pass/Fail determination
* Percentage calculation

### 🗄️ Database Operations

* Store student and result records in MySQL
* Retrieve data using SQL queries
* Use JOIN operations to combine student and result information

### 💻 Command Line Interface

* Menu-driven CLI application
* Easy navigation and user interaction

---

## 🛠️ Technologies Used

* Python
* MySQL
* Object-Oriented Programming (OOP)
* SQL
* MySQL Connector for Python

---

## 🔄 System Workflow

```text
User Input
    │
    ▼
CLI Menu
    │
    ▼
Python Application
    │
    ▼
MySQL Database
    │
    ▼
Student & Result Processing
    │
    ▼
Grade / Pass-Fail Calculation
    │
    ▼
Display Results
```

---

## 📂 Project Structure

```text
student-result-management/
│
├── main.py
├── database.py
├── student.py
├── result.py
├── utils.py
├── requirements.txt
└── README.md
```

*(Modify the structure according to your actual project files.)*

---

## 🗃️ Database Design

### Students Table

| Column     | Description       |
| ---------- | ----------------- |
| student_id | Unique student ID |
| name       | Student name      |
| class      | Student class     |
| age        | Student age       |

### Results Table

| Column     | Description                     |
| ---------- | ------------------------------- |
| result_id  | Unique result ID                |
| student_id | Foreign key from Students table |
| subject    | Subject name                    |
| marks      | Marks obtained                  |

### Relationships

* One student can have multiple subject results.
* JOIN queries are used to retrieve complete student performance reports.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd student-result-management
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL

* Create the required database.
* Create tables for students and results.
* Update database credentials in the project files.

### 4. Run the Application

```bash
python main.py
```

---

## 📝 Sample Operations

* Add Student
* Update Student
* Delete Student
* View Student Details
* Add Result
* Update Result
* View Student Report Card
* Calculate Grades
* Check Pass/Fail Status

---

## 🔮 Future Improvements

* User authentication system
* Export reports to PDF or Excel
* Student search and filtering
* GPA and CGPA calculation
* Graphical User Interface (GUI) version
* Web-based version using Django or Flask

---

## 👨‍💻 Author

Developed as a learning project to strengthen Python programming, Object-Oriented Programming (OOP), MySQL database management, SQL JOIN operations, and CRUD application development.


# LifeOS – A Student Campus Life Manager
**Course:** CSE1021 – Introduction to Problem Solving and Programming
**University:** VIT Bhopal University
**Semester:** Fall Semester 2026–27
**Author:** Sarthak Srivastava

---

## 1. Project Overview
**LifeOS** is a simple command-line student life management system developed in Python for the CSE1021 course project.

The project brings several everyday student activities into one terminal-based application:
* Personal profile and diary
* Task and deadline management
* Class timetable
* Study room booking
* Pocket money management
* Study progress and milestones
The purpose of LifeOS is to demonstrate how basic programming concepts can be combined to solve a practical student-life problem.
The application runs completely in the terminal and does not require an internet connection, database, GUI, or external Python libraries.

---

## 2. Problem Statement
College students often manage different aspects of their daily life separately, such as assignments, classes, study spaces, personal activities, and pocket money.
LifeOS provides a single lightweight terminal application where a student can manage these activities through a simple menu-driven interface.
The system also provides validation and feedback to prevent invalid operations such as duplicate room bookings, overspending, invalid task priorities, empty task names, incorrectly formatted deadlines, and non-numeric entries where a number is expected.

---

## 3. Objectives
The main objectives of LifeOS are:
1. To create a simple student life management system.
2. To apply Python programming concepts to a real-world problem.
3. To divide the application into multiple functional modules.
4. To provide clear input and output through a terminal interface.
5. To implement validation and error handling for common incorrect inputs.
6. To demonstrate the use of functions, modules, lists, dictionaries, loops and conditional statements.
7. To maintain shared student information across different modules.
8. To provide a foundation that can later be extended with persistent storage and additional features.

---

## 4. Main Features

| Module                 | Functionality                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Life Map & Profile** | Displays student name, health, study score and money; maintains a small diary and club membership                  |
| **Action Board**       | Adds, views, completes, deletes and summarises tasks with priority and deadline; groups pending tasks by priority   |
| **Timetable & Rooms**  | Adds and displays subjects and provides study room booking                                                          |
| **Expense Tracker**    | Adds allowance, spends money and prevents spending more than the available balance                                  |
| **Study Progress**     | Completing tasks increases the Study score and activates milestones                                                 |

### Additional Behaviour
* First completed task generates a milestone.
* Reaching a Study score of 50 generates another milestone.
* A study room cannot be booked twice.
* A student cannot join the same club twice.
* Overspending is prevented.
* Invalid priorities and incorrectly formatted deadlines are rejected.
* Empty task names are rejected.
* Non-numeric entries are rejected before conversion, so they no longer stop the program.
* Clear messages are displayed for invalid choices.

---

## 5. Functional Requirements

### FR1 – Profile Management
The system shall:
* Accept and display the student's name.
* Display Health, Study and Money values.
* Display the student's journey diary.
* Allow the student to add a diary/event entry.
* Allow the student to join available clubs.

### FR2 – Task Management
The system shall:
* Add a new task.
* Assign a priority of `high`, `medium`, or `low`.
* Assign a deadline.
* Display existing tasks.
* Mark a task as completed.
* Prevent a completed task from being completed again.
* Delete a task.
* Display a summary of total, completed and pending tasks.
* Display pending tasks grouped by priority.
* Increase the Study score when a task is completed.

### FR3 – Timetable Management
The system shall:
* Add subjects/classes to the timetable.
* Display the current timetable.
* Inform the user when no classes have been added.

### FR4 – Study Room Booking
The system shall:
* Provide three study rooms.
* Allow a student to book an available room.
* Prevent a room from being booked twice.
* Reject invalid room numbers.

### FR5 – Expense Management
The system shall:
* Display the current balance.
* Add pocket money/allowance.
* Record spending.
* Prevent spending greater than the available balance.
* Reject zero, negative or non-numeric amounts.
* Increase Health when money is spent, subject to the Health limit.

---

## 6. Non-Functional Requirements

### NFR1 – Usability
The application should provide a simple menu-driven terminal interface with clear prompts and messages.

### NFR2 – Reliability
The application should prevent invalid operations such as duplicate room bookings, duplicate club membership, overspending, and non-numeric input where a number is expected.

### NFR3 – Maintainability
The program is divided into separate Python modules so that individual features can be modified without changing the entire application.

### NFR4 – Error Handling
The system validates important user inputs and provides meaningful error messages when invalid information is entered.

### NFR5 – Resource Efficiency
The application uses only Python's built-in features and stores its temporary data in memory, resulting in very low resource requirements.

### NFR6 – Portability
The project can run on systems that have Python 3 installed, including Windows, macOS and Linux.

---

## 7. Technologies and Tools

### Programming Language
* Python 3

### Python Concepts Used
* Variables
* Data types
* Input and output
* Operators
* `if`, `elif`, and `else`
* `while` loops
* `for` loops
* Lists
* Dictionaries
* Strings
* Functions
* Modules
* Conditional validation

### Development Tools
* Visual Studio Code
* Git
* GitHub

No external Python libraries are required.

---

## 8. System Architecture
LifeOS follows a simple **modular architecture**. `main.py` calls four feature modules based on the user's menu choice. The modules that require shared student statistics use the values maintained in `student_stats.py`.

```text
                          ┌─────────────────┐
                          │     main.py     │
                          │  Main Menu/UI   │
                          └────────┬────────┘
                                   │
     ┌───────────────┬─────────────┼─────────────┬───────────────┐
     │               │             │             │               │
     ▼               ▼             ▼             ▼               │
┌───────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐    │
│ Life Map  │ │ Action Board│ │ Timetable & │ │   Expense   │    │
│ & Profile │ │    Tasks    │ │    Rooms    │ │   Tracker   │    │
└─────┬─────┘ └──────┬──────┘ └──────┬──────┘ └──────┬──────┘    │
      │              │               │               │           │
      └──────────────┴───────────────┴───────────────┴───────────┘
                                     │
                             ┌───────▼────────┐
                             │student_stats.py│
                             │ Shared Student │
                             │     Values     │
                             └────────────────┘

`main.py` controls the program flow and calls the appropriate feature module based on the user's menu selection.
`student_stats.py` contains shared student values such as name, Health, Study and Money. `action_board.py` also imports `life_map.py` directly, so a completed task can add a milestone straight into the journey diary.

---

## 9. Project Structure

## 9. Project Structure

```text
LifeOs/
├── main.py
├── student_stats.py
├── life_map.py
├── action_board.py
├── timetable_rooms.py
├── expense_tracker.py
├── test_lifeos.py
├── README.md
├── statement.md
└── screenshots/
    ├── main.py.png
    ├── Action board.py.png
    ├── timetable_rooms.py.png
    └── Expense tracker.py.png

### File Description
| File                 | Purpose                                                |
| -------------------- | ------------------------------------------------------- |
| `main.py`            | Main program, menu and program loop                    |
| `student_stats.py`   | Stores shared student values                            |
| `life_map.py`        | Profile, diary and club functionality                   |
| `action_board.py`    | Task management, priorities, deletion, summary and milestones |
| `timetable_rooms.py` | Timetable and study room booking                        |
| `expense_tracker.py` | Pocket money and expense management                     |
| `test_lifeos.py`     | Automated checks for every module                        |
| `statement.md`       | Project problem statement and scope                      |
| `README.md`          | Project documentation                                    |

---

## 10. How the Modules Work Together
The application starts from `main.py`.
The user selects an option from the main menu, and `main.py` calls the corresponding module.

```text
User 
 │ 
 ▼ 
main.py 
 ├── Option 1 ──► life_map.py 
 ├── Option 2 ──► action_board.py ──► life_map.py (writes milestones to diary)
 ├── Option 3 ──► timetable_rooms.py 
 └── Option 4 ──► expense_tracker.py

Every module above also reads and updates the shared values in `student_stats.py`.
For example, when a student completes a task, the Study score is increased in `student_stats.py`. The updated value can then be displayed by the Life Map & Profile module.

---

## 11. Installation
No additional packages or dependencies are required.

### Requirement
Python 3 must be installed.
Check the installation using:


python --version


For macOS/Linux:

python3 --version

---

## 12. Clone the Repository

```bash
git clone https://github.com/Sarthak26Srivastava/LifeOs.git
```

Enter the project directory:

```bash
cd LifeOs
```
---

## 13. Run the Program

On Windows:

```bash
python main.py
```

On macOS/Linux:

```bash
python3 main.py
```

The program will ask for the student's name and display the main menu.

===== LIFEOS MENU =====

1. Life Map & Profile
2. Action Board (Tasks)
3. Timetable & Rooms
4. Expense Tracker
5. Quit

Enter the corresponding menu number and follow the instructions displayed by the program.

---

## 14. Example Session

Welcome to LifeOS! What is your name? Sarthak

===== LIFEOS MENU =====

1. Life Map & Profile
2. Action Board (Tasks)
3. Timetable & Rooms
4. Expense Tracker
5. Quit

Choose an option: 2

Enter add, view, priority, delete or summary: add

Task name: Finish assignment
Priority (high/medium/low): high
Deadline (DD-MM-YYYY): 30-09-2026

--- TASK ADDED --- Finish assignment

---

## 15. Testing
LifeOS was tested in two ways: an automated test file, and manual functional testing of the full program.

### Automated Testing
`test_lifeos.py` replaces the keyboard with a list of prepared answers and calls every function directly, then checks the result with a simple PASS/FAIL comparison. It does not need any typing.

Run it with:

```bash
python test_lifeos.py
```

It currently runs 47 checks across the core LifeOs modules, covering valid inputs, invalid inputs, edge cases, and core functionality. All 47 checks pass successfully.

### Manual Testing
The complete program was also run by hand and checked against the cases below.

| #  | Test                                  | Expected Result                        |
| -- | -------------------------------------- | ---------------------------------------- |
| 1  | Enter `9` at the main menu             | Invalid menu choice message              |
| 2  | Add task with empty name               | Empty-name error                         |
| 3  | Enter priority `urgent`                | Invalid priority message                 |
| 4  | Enter deadline `30-9-2026`              | Invalid date-format message              |
| 5  | Add and complete a valid task          | Task completed and Study increases       |
| 6  | Complete the same task again           | Already-completed message                |
| 7  | Enter task number `99`                 | Task does not exist message              |
| 8  | Enter letters for a task number        | Please-type-a-number message, no crash   |
| 9  | Delete a task                          | Task removed from the list               |
| 10 | View the task summary                  | Correct total, done and pending counts   |
| 11 | Join the same club twice               | Duplicate membership message             |
| 12 | Book the same room twice               | Room unavailable message                 |
| 13 | Book room `9`                          | Invalid room message                     |
| 14 | Spend more than available balance      | Insufficient money message               |
| 15 | Enter a negative amount                | Invalid amount message                   |
| 16 | Enter letters for an amount            | Please-type-the-amount message, no crash |
| 17 | View timetable before adding classes   | No classes message                       |
| 18 | Add a valid class                      | Class added successfully                 |
| 19 | Complete five tasks                    | Study reaches 50 and milestone appears   |
| 20 | Select Quit and enter `n`              | Returns to main menu                     |
| 21 | Select Quit and enter `y`              | Program exits                            |

---

## 16. Screenshots

The `Screenshots/` folder contains sample outputs from the application.

### Main Menu
![alt text](Screenshots/main.py.png)

### Action Board
![alt text](Screenshots/Action%20board.py.png)

### Timetable and Study Rooms

![alt text](Screenshots/timetable_rooms.py.png)

### Expense Tracker

![alt text](Screenshots/Expense%20tracker.py.png)

---

## 17. Error Handling and Validation

LifeOS contains validation for several common user errors.

Examples include:
```
Invalid choice.
Task name cannot be empty.
Invalid priority. Use high, medium or low.
Deadline must look like 30-09-2026.
Task is already completed.
That task does not exist.
Please type a task number.
You already joined this club.
ROOM UNAVAILABLE.
INVALID ROOM.
Not enough money!
Amount must be more than 0.
Please type the amount as a whole number.
```

These checks help prevent incorrect operations and provide feedback to the user.

---

## 18. Current Limitations
The current version has some limitations:
1. Data is stored only in memory.
2. All data is reset when the program closes.
3. Some choices must be entered exactly as displayed.
4. There is currently no database or permanent file storage.
5. Automated testing covers the core modules but is not exhaustive.

These limitations are documented so that they can be addressed in future versions.

---

## 19. Future Enhancements
Possible future improvements include:
* Persistent data storage using files or a database.
* Editing tasks and timetable entries.
* More clubs and study rooms.
* Room booking based on time slots.
* Automatic deadline reminders.
* Search and filtering for tasks.
* Wider automated test coverage.
* Graphical user interface.
* User login and multiple student profiles.

---

## 20. Learning Outcomes
Through this project, the following concepts were practiced:
* Breaking a problem into smaller modules.
* Designing a menu-driven application.
* Using functions to organize program logic.
* Using Python modules and imports.
* Working with lists and dictionaries.
* Applying conditional statements and loops.
* Validating user input, including numeric checks before conversion.
* Handling real-world constraints.
* Managing shared data between modules.
* Writing simple automated tests.
* Using Git and GitHub for project version control.
* Documenting a software project.

---

## 21. GitHub Repository
**Repository:**
https://github.com/Sarthak26Srivastava/LifeOs

The repository contains the source code, automated tests, project documentation, `statement.md`, and screenshots required for the project submission.

---

## 22. Author

**Sarthak Srivastava**
CSE1021 – Introduction to Problem Solving and Programming
VIT Bhopal University
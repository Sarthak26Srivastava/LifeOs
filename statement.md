# LifeOS – Student Campus Life Manager

## Problem Statement

### Problem
College students have many small things to keep track of. There are assignments with deadlines, class timetables, study rooms that may already be occupied, clubs to join, personal activities, and a limited pocket money budget. These things are often managed separately or simply remembered.
When everything is handled separately, it becomes easier to forget a deadline, try to book an occupied room, or lose track of spending. A normal to-do list also focuses mainly on tasks and does not cover other parts of student life.

### Solution
**LifeOS** puts these everyday activities into one small terminal-based program.
A student can manage their profile and diary, tasks, timetable, study rooms, and pocket money from a single menu. The system also gives a Study score that increases when tasks are completed, along with milestone messages to make progress more visible.

The project is intentionally kept simple because its main purpose is to apply the Python programming concepts learned in CSE1021 to a practical problem.

---

## Scope
LifeOS is a terminal-based application designed for **one student during a program session**.
It contains four main functional areas:
1. **Profile and Diary** – view personal information, record events and manage club membership.
2. **Action Board** – create tasks, assign priorities and deadlines, complete tasks, delete tasks, view a task summary and view pending tasks by priority.
3. **Timetable and Rooms** – add subjects, view the timetable and book study rooms.
4. **Expense Tracker** – add allowance, record spending and prevent spending more money than the available balance.
The application also maintains a Study score and Health value that can change based on certain activities.
LifeOS includes input validation and displays messages when an operation is invalid.
The current version has **no graphical interface, database, internet connection or external Python libraries**. Data is stored in memory and is lost when the program closes.

---

## Target Users
The main target users are **college students**, especially first-year students living on campus who want a simple way to organise their academic and everyday activities.
The system is intended for students who need to keep track of:
* Assignments and deadlines
* Classes and subjects
* Study room availability
* Clubs and personal events
* Pocket money
* Basic study progress
The current version is designed for one student rather than multiple users.

---

## High-Level Features
* **Profile:** Displays student name, Health, Study and Money.
* **Diary:** Allows the student to record and view personal journey events.
* **Clubs:** Allows the student to join available clubs and prevents joining the same club twice.
* **Tasks:** Adds tasks with a priority and deadline and allows them to be completed, deleted, or viewed as a short summary.
* **Priority View:** Displays pending tasks grouped into High, Medium and Low priority.
* **Study Progress:** Completing tasks increases the Study score and can trigger milestone messages.
* **Timetable:** Allows subjects to be added and displayed.
* **Study Rooms:** Allows one of three study rooms to be booked and prevents duplicate booking.
* **Expense Tracker:** Allows money to be spent or allowance to be added while preventing overspending.
* **Input Validation:** Provides feedback for common invalid inputs, including non-numeric entries where a number is expected.

---

## Functional Requirements

### FR1 – Main Menu
* The system shall ask the student for their name when the program starts.
* The system shall display the main menu.
* The system shall continue displaying the menu until the student chooses to quit.
* The system shall display an error message for an invalid menu choice.
* The system shall ask for confirmation before quitting.

### FR2 – Profile, Diary and Clubs
* The system shall display the student's name, Health, Study and Money.
* The system shall display the journey diary.
* The system shall allow the student to add a diary event.
* The system shall allow the student to choose from the available Coding Club and Sports Club options.
* The system shall prevent the student from joining the same club twice.
* The system shall display an appropriate message for an unavailable club.

### FR3 – Task Management
* The system shall allow the student to add a task.
* Each task shall contain a name, priority and deadline.
* The system shall accept `high`, `medium` or `low` as task priorities.
* The system shall allow the student to view tasks.
* The system shall allow the student to mark a task as completed.
* The system shall prevent an already completed task from being completed again.
* The system shall allow the student to delete a task.
* The system shall allow the student to view a short summary of total, completed and pending tasks.
* The system shall display an appropriate message when a task number does not exist.
* The system shall display pending tasks grouped by priority.
* Completing a task shall increase the Study score.

### FR4 – Timetable and Study Rooms
* The system shall allow the student to add subjects to the timetable.
* The system shall allow the student to view the timetable.
* The system shall inform the student when no classes have been added.
* The system shall provide three study rooms for booking.
* The system shall allow an available room to be booked.
* The system shall prevent a room from being booked twice.
* The system shall reject an invalid room selection.

### FR5 – Expense Management
* The system shall display the current money balance.
* The system shall allow the student to add an allowance.
* The system shall allow the student to record spending.
* The system shall prevent spending more money than the current balance.
* The system shall reject amounts that are not positive whole numbers.
* The system shall update the displayed balance after a valid transaction.

---

## Non-Functional Requirements

### NFR1 – Usability
The application shall use a simple numbered menu and clear prompts. The allowed values are shown wherever necessary so that a student can understand what to enter.

### NFR2 – Reliability
The system shall prevent invalid operations such as duplicate club membership, duplicate room booking, completing the same task twice and spending more than the available balance.

### NFR3 – Maintainability
The program is divided into separate Python files based on functionality. Each module has a specific responsibility, while shared student values are maintained in one place.

### NFR4 – Error Handling
The system shall validate important user inputs, including checking that a value is numeric before converting it, and shall display a short, understandable message when the input does not meet the expected requirements.

### NFR5 – Performance and Resource Efficiency
The application uses in-memory data and only built-in Python features. Because of its small scope and lightweight operations, normal menu actions respond immediately.

### NFR6 – Portability
The application uses Python 3 and standard terminal input/output, allowing it to run on operating systems that support Python 3.

---

## Basic Workflow

```
Start LifeOS
     ↓
Enter Student Name
     ↓
Display Main Menu
     ↓
Select a Module
     ↓
Perform an Operation
     ↓
Validate Input
     ↓
Update Data
     ↓
Display Result
     ↓
Return to Main Menu
     ↓
Quit?
  ↙       ↘
 No        Yes
 ↓          ↓
Menu      Exit
```

---

## Input and Output

### Inputs
The application accepts:
* Student name
* Menu choices
* Task names
* Task priorities
* Task deadlines
* Task numbers
* Diary events
* Club names
* Subject names
* Study room selections
* Money amounts
* Quit confirmation

### Outputs
The application displays:
* Student profile
* Diary entries
* Club status
* Task information
* Task completion status
* Task summary
* Study score and milestones
* Timetable
* Room booking status
* Current money balance
* Transaction results
* Validation and error messages

---

## Technical Boundaries
The current version deliberately focuses on basic programming rather than a full campus management system.
It does not currently provide:
* Multiple user accounts
* Login or authentication
* A database
* Permanent data storage
* Real-time campus room availability
* Online room booking
* Notifications
* A graphical user interface
* Online payments

Because no database is used, an ER diagram does not apply to this project.
These are considered possible future extensions rather than requirements of the current version.

---

## Current Limitations
* Only one student can use the program during a session.
* Data is stored only in memory and is lost when the program closes.
* Some choices must be entered exactly as displayed.
* The application does not use persistent storage.
* Automated testing covers the core modules; a few manual checks are also used to confirm menu behaviour.

---

## Future Scope
The project can be extended in several ways:
* Save and load data using files.
* Add database support.
* Add editing of tasks, classes and diary events.
* Add task search and filtering.
* Add timetable time slots.
* Add time-based study room reservations.
* Add more clubs and study rooms.
* Add deadline reminders.
* Expand automated testing.
* Add a graphical user interface.
* Support multiple student profiles.

---

## Project Objective
The main objective of LifeOS is to demonstrate how a real-world student problem can be broken into smaller problems and solved using fundamental programming concepts.

The project follows a simple development idea:

**Identify the problem → divide it into modules → design the workflow → implement the features → validate inputs → test the behaviour → document the solution.**

LifeOS is therefore not intended to be a complete college management platform. It is a practical CSE1021 project that combines several everyday student activities into one understandable and modular Python application.
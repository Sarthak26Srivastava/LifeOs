# action_board.py - add tasks, mark them done, view by priority

import student_stats
import life_map
tasks = []   # each task: name, priority, deadline, status (Pending/Done)

def add_task():
    name = input("Task name: ")
    priority = input("Priority (high/medium/low): ")
    deadline = input("Deadline (DD-MM-YYYY): ")
    if name == "":
        print("Task name cannot be empty.")
    elif priority not in ["high", "medium", "low"]:
        print("Invalid priority. Use high, medium or low.")
    elif len(deadline) != 10:   # DD-MM-YYYY is always 10 characters
        print("Deadline must look like 30-09-2026.")
    else:
        tasks.append({"name": name, "priority": priority, "deadline": deadline, "status": "Pending"})
        print("--- TASK ADDED ---", name)

def view_tasks():
    print("--- YOUR TASKS ---")
    if len(tasks) == 0:
        print("No tasks yet.")
        return
    for i in range(len(tasks)):
        task = tasks[i]
        print(i + 1, "-", task["name"], "|", task["status"])
        print("   Priority:", task["priority"], "| Due:", task["deadline"])

    choice = input("Task number to mark done (Enter to skip): ")
    if choice == "":
        return
    if not choice.isdigit():
        print("Please type a task number.")
        return
    task_index = int(choice) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("That task does not exist.")
    elif tasks[task_index]["status"] == "Done":
        print("Task is already completed.")
    else:       
        before = student_stats.study
        tasks[task_index]["status"] = "Done"
        student_stats.study += student_stats.study_gain
        print("--- TASK COMPLETED --- Study is now", student_stats.study)
        if before == 0:
            print("Milestone: first task completed!")
            life_map.life_events.append("Completed first task")
        if before < 50 and student_stats.study >= 50:
            print("Milestone: Study reached 50!")
            life_map.life_events.append("Study reached 50")
                 
def view_by_priority():
    print("--- PRIORITY TASKS ---")
    # high first, then medium, then low - only tasks that are still Pending
    for level in ["high", "medium", "low"]:
        print(level.upper() + ":")
        for task in tasks:
            if task["status"] == "Pending" and task["priority"] == level:
                print("-", task["name"], "| Due:", task["deadline"])
  
def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.")
        return
    for i in range(len(tasks)):
        print(i + 1, "-", tasks[i]["name"])
 
    choice = input("Task number to delete (Enter to skip): ")
    if choice == "":
        return
    if not choice.isdigit():
        print("Please type a task number.")
        return
    task_index = int(choice) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("That task does not exist.")
    else:
        print("--- TASK DELETED ---", tasks[task_index]["name"])
        del tasks[task_index]
 
def task_summary():
    # count the tasks that are done, the same idea as the counting example in Module 3
    total = len(tasks)
    done = 0
    for task in tasks:
        if task["status"] == "Done":
            done = done + 1
    print("--- TASK SUMMARY ---")
    print("Total:", total, "| Done:", done, "| Pending:", total - done)
    if total > 0:
        print("Completed:", done * 100 // total, "percent")   # whole percent

def action_board():
    action = input("Enter add, view, priority, delete or summary:")
    if action == "add":
        add_task()
    elif action == "view":
        view_tasks()
    elif action == "priority":
        view_by_priority() 
    elif action == "delete":
        delete_task()
    elif action == "summary":
        task_summary()
    else:
        print("Invalid choice.")
# action_board.py
# Manages tasks: add, view, complete, and view by priority.

import student_stats
import life_map

tasks = []   # each task: name + priority + deadline + done status


def action_board():
    global tasks

    action = input("Type add, view, or priority: ")

    if action == "add":
        task_name = input("Task name: ")
        if task_name == "":
            return
        priority = input("Priority (high/medium/low): ")
        deadline = input("Deadline (DD-MM-YYYY): ")
        if priority != "high" and priority != "medium" and priority != "low":
            print("Invalid priority.")
            return
        new_task = {"name": task_name, "priority": priority, "deadline": deadline, "done": False}
        tasks = tasks + [new_task]
        print("--- TASK ADDED ---")
        print(task_name)

    if action == "view":
        print("--- YOUR TASKS ---")
        if len(tasks) == 0:
            print("No tasks yet.")
            return
        for i in range(len(tasks)):
            if tasks[i]["done"] == True:
                status = "Done"
            else:
                status = "Pending"
            print(i + 1, "-", tasks[i]["name"], "| Priority:", tasks[i]["priority"], "| Deadline:", tasks[i]["deadline"], "|", status)

        task_choice = input("Task number to mark done (Enter to skip): ")
        if task_choice == "":
            return
        task_index = int(task_choice) - 1
        if task_index < 0 or task_index >= len(tasks):
            print("That task does not exist.")
            return
        if tasks[task_index]["done"] == True:
            print("Task is already completed.")
            return

        tasks[task_index]["done"] = True
        student_stats.study = student_stats.study + student_stats.study_gain
        print("--- TASK COMPLETED ---")
        print("Study is now", student_stats.study)

        done_count = 0
        for t in tasks:
            if t["done"] == True:
                done_count = done_count + 1
        if done_count == 1:
            print("Milestone: first task completed!")
            life_map.life_events = life_map.life_events + ["Completed first task"]
        if student_stats.study >= 50 and student_stats.study - student_stats.study_gain < 50:
            print("Milestone: Study reached 50!")
            life_map.life_events = life_map.life_events + ["Study reached 50"]

    if action == "priority":
        print("--- PRIORITY TASKS ---")
        print("HIGH:")
        for task in tasks:
            if task["done"] == False and task["priority"] == "high":
                print("-", task["name"], "| Due:", task["deadline"])
        print("MEDIUM:")
        for task in tasks:
            if task["done"] == False and task["priority"] == "medium":
                print("-", task["name"], "| Due:", task["deadline"])
        print("LOW:")
        for task in tasks:
            if task["done"] == False and task["priority"] == "low":
                print("-", task["name"], "| Due:", task["deadline"])
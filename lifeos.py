# lifeos.py
# LifeOS - Simple Student Organizer + XP System
# CSE1021 Project

tasks = []
notes = []

first_step_done = False
task_master_done = False
early_player_done = False

available_slots = {"9-10", "10-11", "11-12", "2-3", "3-4", "4-5"}
booked_slots = {}

player_name = input("Welcome to LifeOS! What is your name? ")
level = 1
xp = 0
xp_needed = 100
health = 100
study = 0
fitness = 0

while True:
    print("")
    print("===== LIFEOS MENU =====")
    print("1. View profile")
    print("2. Add task")
    print("3. View tasks")
    print("4. Complete a task")
    print("5. Add note")
    print("6. View notes")
    print("7. Delete note")
    print("8. View achievements")
    print("9. Daily summary")
    print("10. Book a study slot")
    print("11. View study slots")
    print("12. Cancel a study slot")
    print("13. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("")
        print("========================================")
        print("PLAYER")
        print("Name:", player_name)
        print("Level:", level)
        print("XP:", xp, "/", xp_needed)
        print("Health:", health)
        print("Study:", study)
        print("Fitness:", fitness)
        print("========================================")

    elif choice == "2":
        name = input("Task name: ")
        if name == "":
            print("Task name cannot be empty.")
        else:
            category = input("Category (Study/Fitness/General): ")
            category = category.capitalize()
            if category != "Study" and category != "Fitness":
                category = "General"
            task = {"name": name, "category": category, "done": False}
            tasks = tasks + [task]
            print("Task added.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("Your tasks:")
            for i in range(len(tasks)):
                if tasks[i]["done"] == True:
                    status = "Done"
                else:
                    status = "Pending"
                print(i + 1, "-", tasks[i]["name"], "|", tasks[i]["category"], "|", status)

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            print("Your tasks:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i]["name"])

            task_choice = int(input("Which task number did you complete? "))
            index = task_choice - 1

            if index >= 0 and index < len(tasks):
                if tasks[index]["done"] == True:
                    print("That task is already done.")
                else:
                    tasks[index]["done"] = True

                    if tasks[index]["category"] == "Study":
                        xp = xp + 40
                        study = study + 5
                        if study > 100:
                            study = 100
                    elif tasks[index]["category"] == "Fitness":
                        xp = xp + 30
                        fitness = fitness + 5
                        if fitness > 100:
                            fitness = 100
                    else:
                        xp = xp + 20

                    print("Task completed!")

                    while xp >= xp_needed:
                        xp = xp - xp_needed
                        level = level + 1
                        xp_needed = level * 100
                        print("LEVEL UP! You are now level", level)

                    completed_count = 0
                    for t in tasks:
                        if t["done"] == True:
                            completed_count = completed_count + 1

                    if completed_count >= 1 and first_step_done == False:
                        first_step_done = True
                        print("Achievement unlocked: FIRST STEP")

                    if completed_count >= 5 and task_master_done == False:
                        task_master_done = True
                        print("Achievement unlocked: TASK MASTER")

                    if level >= 5 and early_player_done == False:
                        early_player_done = True
                        print("Achievement unlocked: EARLY PLAYER")
            else:
                print("That task number does not exist.")

    elif choice == "5":
        text = input("Enter your note: ")
        if text == "":
            print("Note cannot be empty.")
        else:
            notes = notes + [text]
            print("Note added.")

    elif choice == "6":
        if len(notes) == 0:
            print("No notes yet.")
        else:
            print("Your notes:")
            for i in range(len(notes)):
                print(i + 1, "-", notes[i])

    elif choice == "7":
        if len(notes) == 0:
            print("No notes yet.")
        else:
            print("Your notes:")
            for i in range(len(notes)):
                print(i + 1, "-", notes[i])

            note_choice = int(input("Which note number do you want to delete? "))
            index = note_choice - 1
            if index >= 0 and index < len(notes):
                print("Deleted:", notes[index])
                del notes[index]
            else:
                print("That note number does not exist.")

    elif choice == "8":
        if first_step_done == False and task_master_done == False and early_player_done == False:
            print("No achievements unlocked yet.")
        else:
            print("Achievements unlocked:")
            if first_step_done == True:
                print("- FIRST STEP")
            if task_master_done == True:
                print("- TASK MASTER")
            if early_player_done == True:
                print("- EARLY PLAYER")

    elif choice == "9":
        total = len(tasks)
        completed = 0
        for t in tasks:
            if t["done"] == True:
                completed = completed + 1
        pending = total - completed

        print("DAILY SUMMARY")
        print("Total tasks:", total)
        print("Completed:", completed)
        print("Pending:", pending)

    elif choice == "10":
        print("Available slots:")
        for slot in available_slots:
            print("-", slot)

        chosen_slot = input("Which slot do you want to book? ")

        if chosen_slot in available_slots:
            subject = input("What will you study in this slot? ")
            available_slots.remove(chosen_slot)
            booked_slots[chosen_slot] = subject
            print("Slot booked:", chosen_slot, "for", subject)
        else:
            print("That slot is not available.")

    elif choice == "11":
        print("Booked slots:")
        if len(booked_slots) == 0:
            print("No slots booked yet.")
        else:
            for slot in booked_slots:
                print(slot, "-", booked_slots[slot])

        print("Free slots:")
        if len(available_slots) == 0:
            print("No free slots left.")
        else:
            for slot in available_slots:
                print("-", slot)

    elif choice == "12":
        cancel_slot = input("Which slot do you want to cancel? ")

        if cancel_slot in booked_slots:
            del booked_slots[cancel_slot]
            available_slots.add(cancel_slot)
            print("Slot cancelled:", cancel_slot)
        else:
            print("That slot was not booked.")

    elif choice == "13":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again.")
# lifeos.py
# LifeOS - A Student Campus Life Manager
# CSE1021 Project

player_name = input("Welcome to LifeOS! What is your name? ")
health, study, money = 100, 0, 500
study_gain = 10   # how much Study increases per completed task

life_events = ["Joined College"]     # things that happened
joined_clubs = []                    # clubs the student joined
tasks = []                           # each task: name + done status
class_schedule = []                  # subjects added to timetable
booked_rooms = []                    # rooms currently booked

while True:
    print("")
    print("===== LIFEOS MENU =====")
    print("1. Life Map & Profile")
    print("2. Action Board (Tasks)")
    print("3. Timetable & Rooms")
    print("4. Expense Tracker")
    print("5. Quit")
    choice = input("Choose an option: ")

    if choice == "5":
        confirm = input("Are you sure you want to quit? (y/n): ")
        if confirm == "y":
            print("Goodbye,", player_name, "!")
            break

    elif choice == "1":
        print("--- PROFILE ---")
        print("Name:", player_name, "| Health:", health, "| Study:", study, "| Money: Rs", money)
        print("Joined Clubs:")
        if len(joined_clubs) == 0:
            print("- None yet")
        else:
            for c in joined_clubs:
                print("-", c)
        print("--- YOUR JOURNEY ---")
        for event in life_events:
            print("-", event)

        action = input("Type add to log an event, or club to join one: ")
        if action == "add":
            event = input("What happened? ")
            if event != "":
                life_events = life_events + [event]
                print("--- EVENT ADDED ---")
                print(event)
        elif action == "club":
            club_name = input("Enter club name (Coding Club / Sports Club): ")
            if club_name not in joined_clubs:
                joined_clubs = joined_clubs + [club_name]
                life_events = life_events + ["Joined " + club_name]
                print("--- CLUB JOINED ---")
                print(club_name)
            else:
                print("You already joined this club.")

    elif choice == "2":
        action = input("Type add to create a task, or view to see your tasks: ")
        if action == "add":
            task_name = input("Task name: ")
            if task_name != "":
                tasks = tasks + [{"name": task_name, "done": False}]
                print("--- TASK ADDED ---")
                print(task_name)
        elif action == "view":
            print("--- YOUR TASKS ---")
            if len(tasks) == 0:
                print("No tasks yet.")
            else:
                for i in range(len(tasks)):
                    if tasks[i]["done"] == True:
                        status = "Done"
                    else:
                        status = "Pending"
                    print(i + 1, "-", tasks[i]["name"], "[", status, "]")

                task_choice = input("Task number to mark done (or press enter to skip): ")
                if task_choice != "":
                    task_index = int(task_choice) - 1
                    if task_index >= 0 and task_index < len(tasks):
                        tasks[task_index]["done"] = True
                        study = study + study_gain
                        print("--- TASK COMPLETED ---")
                        print("Study is now", study)

                        done_count = 0
                        for t in tasks:
                            if t["done"] == True:
                                done_count = done_count + 1
                        if done_count == 1:
                            print("Milestone: first task completed!")
                            life_events = life_events + ["Completed first task"]
                        if study >= 50 and study - study_gain < 50:
                            print("Milestone: Study reached 50!")
                            life_events = life_events + ["Study reached 50"]
                    else:
                        print("That task number does not exist.")

    elif choice == "3":
        sub = input("Type class to add a subject, or room to book one: ")
        if sub == "class":
            subject_name = input("Subject name: ")
            class_schedule = class_schedule + [subject_name]
            print("--- CLASS ADDED ---")
            print(subject_name)
        elif sub == "room":
            room_name = input("Book Room 1, Room 2, or Room 3? ")
            if room_name in booked_rooms:
                print("--- ROOM UNAVAILABLE ---")
            else:
                booked_rooms = booked_rooms + [room_name]
                print("--- ROOM BOOKED ---")
                print(room_name)

    elif choice == "4":
        print("--- EXPENSE TRACKER ---")
        print("Current Balance: Rs", money)
        action = input("Type spend or add: ")
        if action == "spend":
            amount = int(input("Amount spent: Rs"))
            money = money - amount
            health = health + 10
            print("--- EXPENSE LOGGED ---")
            print("Remaining money: Rs", money)
        elif action == "add":
            amount = int(input("Allowance received: Rs"))
            money = money + amount
            print("--- MONEY ADDED ---")
            print("Total money: Rs", money)

    else:
        print("Invalid choice. Try again!")
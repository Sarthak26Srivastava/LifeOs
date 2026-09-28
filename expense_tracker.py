# expense_tracker.py


import student_stats

def expense_tracker():
    print("--- EXPENSE TRACKER ---")
    print("Current Balance: Rs", student_stats.money)
    action = input("Enter 'spend' to spend money or 'add' to add money: ")

    if action == "spend":
        amount = int(input("Amount spent: Rs "))
        if amount > student_stats.money:
            print("Not enough money!")
            return
        student_stats.money = student_stats.money - amount
        student_stats.health = student_stats.health + 10   # good food, small health boost
        print("--- EXPENSE LOGGED ---")
        print("Remaining money: Rs", student_stats.money)

    elif action == "add":
        amount = int(input("Allowance received: Rs"))
        student_stats.money = student_stats.money + amount
        print("--- MONEY ADDED ---")
        print("Total money: Rs", student_stats.money)
    else:
        print("Invalid choice.")
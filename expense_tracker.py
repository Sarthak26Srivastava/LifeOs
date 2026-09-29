# expense_tracker.py


import student_stats

def expense_tracker():
    print("--- EXPENSE TRACKER ---")
    print("Current Balance: Rs", student_stats.money)
    action = input("Enter 'spend' to spend money or 'add' to add money: ")

    if action not in ["spend", "add"]:
        print("Invalid choice.")
        return
 
    # Check the input first so letters don't cause an error when converting to int
    amount_text = input("Amount: Rs ") # ask for the amount only
    if not amount_text.isdigit():      
        print("Please type the amount as a whole number.")
        return
    amount = int(amount_text)        # convert the text into an integer 
 
    if amount <= 0:
        print("Amount must be more than 0.")
    elif action == "spend" and amount > student_stats.money:
        print("Not enough money!")
    elif action == "spend":
        student_stats.money -= amount
        student_stats.health += 10 
        if student_stats.health > 100:
            student_stats.health = 100     # Food give a small health boost
        print("--- EXPENSE LOGGED ---")
        print("Remaining money: Rs", student_stats.money)
    
    elif action == "add":
        student_stats.money += amount

        print("--- MONEY ADDED ---")
        print("Total money: Rs", student_stats.money)
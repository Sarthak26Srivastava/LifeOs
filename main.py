# main.py
# LifeOS - A Student Campus Life Manager (CSE1021 Project)
# Run file: python main.py 
# Shows the main menu and runs all  the right function from each module.

import student_stats
from life_map import life_map
from action_board import action_board
from timetable_rooms import timetable_and_rooms
from expense_tracker import expense_tracker

# Store the student's name in student_stats
student_stats.student_name = input("Welcome to LifeOS! What is your name? ")

# Main program loop
while True:
    print("")
    print("===== LIFEOS MENU =====")
    print("1. Life Map & Profile")
    print("2. Action Board (Tasks)")
    print("3. Timetable & Rooms")
    print("4. Expense Tracker")
    print("5. Quit")
    
    # getting user input
    choice = input("Choose an option: ")
    if choice == "5":
        confirm = input("Are you sure you want to quit? (y/n): ")
        if confirm == "y" or confirm == "Y":  # Accept both lowercase and uppercase Y
            print("Goodbye,", student_stats.student_name, "!")
            break         # break the loop
            
    elif choice == "1":
        life_map()
    elif choice == "2":
        action_board()
    elif choice == "3":
        timetable_and_rooms()
    elif choice == "4":
        expense_tracker()
    else:
        print("Invalid choice. Try again!")
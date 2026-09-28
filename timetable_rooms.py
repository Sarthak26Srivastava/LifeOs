# timetable_rooms.py

class_schedule = []  
booked_rooms = []     

def add_class():
    subject_name = input("Enter Subject name: ")
    if subject_name == "":
        print("Subject name cannot be empty.")
        return
    class_schedule.append(subject_name)
    print("--- CLASS ADDED ---")
    print(subject_name)


def book_room():
    
    room_name = input("Choose study room 1, study room 2, or study room 3: ")

    # Only three study rooms are available
    if room_name not in ["study room 1", "study room 2", "study room 3"]:
        print("--- INVALID ROOM ---")
        print("Please choose study room 1, study room 2, or study room 3.")
        return
    if room_name in booked_rooms:
        print("--- ROOM UNAVAILABLE ---")
        print(room_name, "is already booked.")
        return
    booked_rooms.append(room_name)
    print("--- ROOM BOOKED ---")
    print(room_name)


def timetable_and_rooms():
    choice = input("Enter 'class' to add a subject or 'room' to book a room: ")

    if choice == "class":
        add_class()
    elif choice == "room":
        book_room()
    else:
        print("Invalid choice.")
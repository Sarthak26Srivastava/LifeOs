# life_map.py

import student_stats

life_events = ["Joined College"]   
joined_clubs = []                 

def life_map():
    
    print("--- PROFILE ---")
    print("Name:", student_stats.student_name)
    print("Health:", student_stats.health)
    print("Study:", student_stats.study)
    print("Money: Rs", student_stats.money)

    
    print("Joined Clubs:")
    if len(joined_clubs) == 0:
        print("- None yet")
    else:
        for c in joined_clubs:
            print("-", c)

    
    print("--- YOUR JOURNEY ---")
    for event in life_events:
        print("-", event)

    action = input("Enter 'add' for an event, or 'club' to join one: ")
    
    if action == "add":
        event = input("What happened? ")
        if event == "":
            print("Event cannot be empty.")
            return
        life_events.append(event)
        print("--- EVENT ADDED ---")
        print(event)

    elif action == "club":
        club_name = input("Club name (Coding Club / Sports Club): ")
        if club_name in joined_clubs:
            print("You already joined this club.")
            return
        joined_clubs.append(club_name)
        life_events.append("Joined " + club_name)
        print("--- CLUB JOINED ---")
        print(club_name)
    else:
        print("Invalid code")
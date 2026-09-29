# life_map.py
# Shows the student's profile and keeps a small diary ("journey") of
# what has happened, including the clubs joined.

import student_stats

life_events = ["Joined College"]   
joined_clubs = []                  # clubs the student has joined


def life_map():
    # Show the profile details stored in student_stats
    print("--- PROFILE ---")
    print("Name:", student_stats.student_name)
    print("Health:", student_stats.health)
    print("Study:", student_stats.study)
    print("Money: Rs", student_stats.money)

    # then the clubs (say so if there are none yet)
    print("Joined Clubs:")
    if len(joined_clubs) == 0:
        print("- None yet")
    else:
        for c in joined_clubs:
            print("-", c)

   # Show the student's journey
    print("--- YOUR JOURNEY ---")
    for event in life_events:
        print("-", event)

    action = input("Enter 'add' to log an event, or 'club' to join one: ")

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
        # only these two clubs exist
        if club_name not in ["Coding Club", "Sports Club"]:
            print("Club not found.")
            return
        if club_name in joined_clubs:
            print("You already joined this club.")
            return
        joined_clubs.append(club_name)
        life_events.append("Joined " + club_name)   # joining is also a life event
        print("--- CLUB JOINED ---")
        print(club_name)

    else:
        print("Invalid choice.")
# test_lifeos.py
# Simple checks for LifeOS. Run it with:  python test_lifeos.py
# The real input() is swapped for a fake one that hands out answers I prepare in advance, so every function can run without any typing.
# Each check prints PASS or FAIL. The program messages in between are just the normal output of the functions being tested.

import builtins
import student_stats
import life_map
import action_board
import timetable_rooms
import expense_tracker

answers = []    # answers the fake input will give, in order
position = 0    # which answer comes next
passed = 0
failed = 0

def fake_input(prompt=""):
    global position
    value = answers[position]
    position = position + 1
    return value

builtins.input = fake_input

def run(function, given):
   # Give the function its test inputs
    global answers, position
    answers = given
    position = 0
    function()


def check(name, condition):
    global passed, failed
    if condition:
        passed = passed + 1
        print("PASS -", name)
    else:
        failed = failed + 1
        print("FAIL -", name)

def reset():
    # Reset everything before each test group
    student_stats.health = 50
    student_stats.study = 0
    student_stats.money = 500
    life_map.life_events = ["Joined College"]
    life_map.joined_clubs = []
    action_board.tasks = []
    timetable_rooms.class_schedule = []
    timetable_rooms.booked_rooms = []

board = action_board.action_board
diary = life_map.life_map
rooms = timetable_rooms.timetable_and_rooms
money = expense_tracker.expense_tracker

print("##### Action Board #####")
reset()
run(board, ["add", "Finish assignment", "high", "30-09-2026"])
check("a valid task is added", len(action_board.tasks) == 1)
check("a new task starts as Pending", action_board.tasks[0]["status"] == "Pending")
run(board, ["add", "", "high", "30-09-2026"])
check("an empty task name is rejected", len(action_board.tasks) == 1)
run(board, ["add", "Read", "urgent", "30-09-2026"])
check("a wrong priority is rejected", len(action_board.tasks) == 1)
run(board, ["add", "Gym", "low", "3-9-2026"])
check("a wrong deadline is rejected", len(action_board.tasks) == 1)
run(board, ["view", "abc"])
check("letters as a task number do not crash or change anything", student_stats.study == 0)
run(board, ["view", "99"])
check("a task number that does not exist changes nothing", student_stats.study == 0)
run(board, ["view", ""])
check("pressing Enter skips marking a task", student_stats.study == 0)
run(board, ["view", "1"])
check("marking a task done sets it to Done", action_board.tasks[0]["status"] == "Done")
check("marking a task done raises Study by 10", student_stats.study == 10)
check("the first task milestone goes into the journey", "Completed first task" in life_map.life_events)
run(board, ["view", "1"])
check("a task already done cannot give Study twice", student_stats.study == 10)
for n in range(2, 6):
    run(board, ["add", "Task " + str(n), "medium", "01-10-2026"])
    run(board, ["view", str(n)])
check("five finished tasks give Study 50", student_stats.study == 50)
check("the Study 50 milestone appears once", life_map.life_events.count("Study reached 50") == 1)
check("the first task milestone appears once", life_map.life_events.count("Completed first task") == 1)
run(board, ["priority"])
check("the priority view runs", True)
run(board, ["summary"])
check("the summary runs", True)
run(board, ["x"])
check("a wrong action changes nothing", len(action_board.tasks) == 5)

print("##### Delete task #####")
reset()
run(board, ["add", "First", "high", "30-09-2026"])
run(board, ["add", "Second", "low", "01-10-2026"])
run(board, ["delete", "abc"])
check("letters as a delete number change nothing", len(action_board.tasks) == 2)
run(board, ["delete", "99"])
check("a delete number that does not exist changes nothing", len(action_board.tasks) == 2)
run(board, ["delete", ""])
check("pressing Enter skips deleting", len(action_board.tasks) == 2)
run(board, ["delete", "1"])
check("deleting task 1 leaves one task", len(action_board.tasks) == 1)
check("the right task was deleted", action_board.tasks[0]["name"] == "Second")
run(board, ["delete", "1"])
run(board, ["delete"])
check("deleting from an empty list is safe", len(action_board.tasks) == 0)

print("##### Life Map #####")
reset()
run(diary, ["add", "Won a quiz"])
check("a life event is added", "Won a quiz" in life_map.life_events)
run(diary, ["add", ""])
check("an empty life event is rejected", len(life_map.life_events) == 2)
run(diary, ["club", "Coding Club"])
check("a club can be joined", "Coding Club" in life_map.joined_clubs)
check("joining a club is written in the journey", "Joined Coding Club" in life_map.life_events)
run(diary, ["club", "Coding Club"])
check("a club cannot be joined twice", life_map.joined_clubs.count("Coding Club") == 1)
run(diary, ["club", "Chess Club"])
check("an unknown club is rejected", len(life_map.joined_clubs) == 1)
run(diary, ["x"])
check("a wrong action changes nothing", len(life_map.joined_clubs) == 1)

print("##### Timetable and Rooms #####")
reset()
run(rooms, ["class", "Python"])
check("a subject is added to the timetable", "Python" in timetable_rooms.class_schedule)
run(rooms, ["class", ""])
check("an empty subject is rejected", len(timetable_rooms.class_schedule) == 1)
run(rooms, ["view"])
check("the timetable view runs", True)
run(rooms, ["room", "study room 1"])
check("a study room can be booked", "study room 1" in timetable_rooms.booked_rooms)
run(rooms, ["room", "study room 1"])
check("a room cannot be booked twice", timetable_rooms.booked_rooms.count("study room 1") == 1)
run(rooms, ["room", "study room 9"])
check("a room that does not exist is rejected", len(timetable_rooms.booked_rooms) == 1)
run(rooms, ["x"])
check("a wrong choice changes nothing", len(timetable_rooms.booked_rooms) == 1)

print("##### Expense Tracker #####")
reset()
run(money, ["spend", "50"])
check("spending 50 leaves 450", student_stats.money == 450)
check("spending raises Health by 10", student_stats.health == 60)
run(money, ["spend", "9999"])
check("spending more than the balance is refused", student_stats.money == 450)
run(money, ["spend", "abc"])
check("letters as an amount are refused", student_stats.money == 450)
run(money, ["spend", "0"])
check("an amount of 0 is refused", student_stats.money == 450)
run(money, ["add", "100"])
check("adding 100 gives 550", student_stats.money == 550)
run(money, ["add", "-5"])
check("a negative amount is refused", student_stats.money == 550)
run(money, ["x"])
check("a wrong choice changes nothing", student_stats.money == 550)
reset()
for n in range(6):
    run(money, ["spend", "10"])
check("Health never goes above 100", student_stats.health == 100)

print("")
print("Passed:", passed, "| Failed:", failed)
# Task 1

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

# Task 2 with Task 3 

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        choice = input("you see two paths ahead! go left or right?")
        if choice == "left":
            print("You find a hidden treasure!")
        elif choice == "right":
            print("Dead end with man-eating spiders!")
        else:
            pass
    elif action == "proceed in the dark":
        print("You got lost and tangled in spider webs!")
    else:
        pass
else:
    pass
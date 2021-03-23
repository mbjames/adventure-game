import room_questions
import traps


def you_win():
    print("\n You made your way to a clearing.")
    print(" A boat was waiting and took you to safety.")

    game_over()


def game_over():
    print("\n Would you like to play again? (y or n)")

    answer = input("\n > ")

    if answer == "y":
        start_room()

    elif answer == "n":
        exit()

    else:
        game_over()


def final_room():
    room_questions.final_room()

    answer = input("\n > ")

    if answer == "1":
        print(traps.trap_door)

        game_over()

    elif answer == "2":
        print(traps.trap_fire)

        game_over()

    elif answer == "3":
        print(traps.trap_arrows)

        game_over()

    elif answer == "4":
        you_win()

    elif answer == "5":
        print(traps.trap_spikes)

        game_over()

    else:
        final_room()


def ruby_room():
    room_questions.ruby_questions()

    answer = input("\n > ")

    if answer == "1":
        print(traps.trap_spikes)

        game_over()

    elif answer == "2":
        final_room()

    else:
        ruby_room()


def sand_room():
    room_questions.sand_questions()

    answer = input("\n > ")

    if answer == "1":
        final_room()

    elif answer == "2":
        print(traps.trap_door)

        game_over()

    else:
        sand_room()


def goblin_room():
    room_questions.goblin_questions()

    answer = input("\n > ")

    if answer == "1":
        print(traps.trap_fire)

        game_over()

    elif answer == "2":
        print(traps.trap_arrows)

        game_over()

    elif answer == "3":
        ruby_room()

    elif answer == "4":
        sand_room()


def dungeon_room():
    room_questions.dungeon_questions()

    answer = input("\n > ")

    if answer == "1":
        you_win()

    elif answer == "2":
        goblin_room()

    else:
        dungeon_room()


def vine_room():
    room_questions.vine_questions()

    answer = input("\n > ")

    if answer == "1":
        print("\n The vines wrapped around you quickly and you died.")

        game_over()

    elif answer == "2":
        print("\n The vines moved to avoid the fire and you proceeded through the door.")

        dungeon_room()

    else:
        vine_room()


def bear_room():
    room_questions.bear_questions()

    answer = input("\n > ")

    if answer == "1":
        print("\n The bear lashed out in anger and you died.")

        game_over()

    elif answer == "2":
        print("\n The bear ran an hid in a corner and you proceeded through the door.")

        vine_room()

    else:
        bear_room()


def monster_room():
    room_questions.monster_questions()

    answer = input("\n > ")

    if answer == "1":
        print("\n The monster ran an hid in a corner and you proceeded through the door.")

        vine_room()

    elif answer == "2":
        print("\n The monster lashed out in anger and you died.")

        game_over()

    else:
        monster_room()


def diamond_room():
    room_questions.diamond_questions()

    answer = input("\n > ")

    if answer == "1":
        print(traps.trap_spikes)

        game_over()

    elif answer == "2":
        print(traps.trap_door)

        game_over()

    else:
        diamond_room()


def start_room():
    room_questions.start_questions()

    answer = input("\n > ")

    if answer == "1":
        bear_room()

    elif answer == "2":
        monster_room()

    elif answer == "3":
        diamond_room()

    elif answer == "4":
        print(traps.trap_door)

        game_over()

    else:
        start_room()


start_room()

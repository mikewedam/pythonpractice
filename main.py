print('''
    Game Instructions
    Start - To start car
    Stop - To stop car
    Exit - To end game
''')
car = "start"
started = False
while car == "start":
    control = input(">")
    if control == "start":
        if started:
            print("car already started")
        else:
            started = True
            print("Car has started...")
    elif control == "stop":
        if control == "stop":
            if not started:
                print("car already stopped")
            else:
                started = False
                print("Car has stopped")
    elif control == "brake":
        if control == "brake":
            if not started:
                print("brakes applied")
            else:
                started = False
                print("Car has stopped")
    elif control == "quit":
        print("You quit the game.")
        break
    else:
        print("I do not understand!")

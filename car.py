car = "start"
started = False
while car =="start":
    control = input(">")
    if control == "start":
        if started:
            print("car already started.")
        else:
            started = True
            print("Car has started...")
    elif control == "stop":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car has stopped.")
    elif control == "quit":
        print("You have quit the game.")
        break
    elif   control == "help":
        print('''
start to start the car.
stop to stop the car. 
quit to exit the game.
help how to play.''')
        break
    else:
        print("I don't understand that.")

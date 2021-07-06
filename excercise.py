#weight_lbs = input("Enter weight lbs ")
#weight_kg = 0.45 * int(weight_lbs)
#print(weight_kg)

#nsg = "I am a car entusiast"
#print(nsg.upper())
#print(nsg.replace("car","automobile"))
#print(nsg.find("c"))

#temperature = 30
#if temperature > 30:
 #   print("It's a hot day.")
#elif temperature < 10:
 #   print("It's a cold day.")
#else:
 #   print("It's neither hot nor cold.")


#name = "Michael"

#if len(name) < 3:
 #   print("Name must be at least 3 characters long.")
#elif len(name) > 50:
 #   print("Name can be a maximum of 50 characters.")
#else:
  #  print(name + " is a nice name.")

#weight = int(input("Weight: "))
#unit = input('lbs(L) or kilo(K): ')
#if unit.upper() == "L":
 #   converted = weight * 0.45
  #  print(f"You are {converted} kilos.")
#else:
 #   converted = weight / 0.45
  #  print(f"You are {converted} pounds.")

#i = 2
#while i <= 100:
 #   print(i)
  #  i = i + 2
#print("Done")

#Guessing Game
#secret_number = 10
#Guess_count = 0
#Guess_limit = 3
#while Guess_count < Guess_limit:
 #   Guess = int(input("Guess: "))
  #  Guess_count += 1
   # if Guess == secret_number:
    #    print("You won")
     #   break
#else:
 #   print("You lost.Try again!")

#car game
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



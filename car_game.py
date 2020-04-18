car_started = False
car_stopped = True
while (1):
    command = input("> ")
    if command == "help":
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif command == "start":
        if car_started:
            print("The car has already started")
        else:
            print('The car has started.')
            car_started = True
            car_stopped = False
    elif command == "stop":
        if car_stopped:
            print("The car has already stopped")
        else:
            print("The car has stopped.")
            car_stopped = True
            car_started = False
    elif command == "quit":
        break
    else:
        print ("I don't understand that.")

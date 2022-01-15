command = ""
started = False
while command != 'quit':
    command = input('>> ').lower()
    if command == 'start':
        if started:
            print('Car has been already started!')
        else:
            started = True
            print('Car has started!...')
    elif command == 'stop':
        if not started:
            print('Car is already stopped!')
        else:
            started = False
            print('Car has stopped')
    elif command == 'help':
        print('''start - car will be started
stop - car will be stopped 
quit - will quit the game''')
    elif command == 'quit' :
        break
    else:
        print("Sorry I don't understand ")
print("You've quit the game ")
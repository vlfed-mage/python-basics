i = 1

while i <= 5:
    print('*' * i)
    i = i + 1
print('Done')

# guessing game

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess number: '))
    guess_count += 1
    if guess == secret_number:
        print('Yes! You won!')
        break
    else:  # belongs to the if statement
        print('Sorry, try again')
else:  # belongs to the while statement
    print('Sorry, you failed...')


# car game
started = False
stopped = False

while True:
    command = input('> ').lower()
    if command == 'help':
        print('''
        start - to start the car
        stop - to stop the car
        quit - to exit
        ''')
    elif command == 'start':
        if started:
            print('Warning: Car is already started! Ready to go!')
        else:
            started = True
            stopped = False
            print('Car started... Ready to go!')
    elif command == 'stop':
        if stopped:
            print('Warning: Car is already stopped!')
        else:
            stopped = True
            started = False
            print('Car stopped')
    elif command == 'quit':
        break
    else:
        print('I don\'t understand that... Type help for getting more information')

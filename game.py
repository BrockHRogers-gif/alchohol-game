Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print('Welcome to the alcohol consequence game. Press A, then enter to start')

command = input('')

while command != 'A':
    print('Please type capital "A"')
    command = input('')

print("You are at a party and see multiple drinks in front of you.")
print("You're over 18, have a full licence, and will still have to drive home later.")
print("The drinks are:")
print("- 30ml shots of high-strength spirits")
print("- Cans of full-strength beer")
print("- Well-poured glasses of wine")
print()
print('Type SHOT, BEER, GLASS, or NA when you are finished.')

ba = 0.0
total_drinks = 0

while True:

    command = input('\nWhat drink would you like? ').upper()

    if command == 'NA':
        break

    elif command == 'SHOT':
        drink = '30ml shot'
        alcohol = 0.3

    elif command == 'BEER':
        drink = 'can of full-strength beer'
        alcohol = 1.4

    elif command == 'GLASS':
        drink = 'glass of wine'
        alcohol = 1.0

    else:
        print('Please type SHOT, BEER, GLASS, or NA.')
        continue

    try:
        amount = int(input(f'How many {drink}s? '))

        if amount <= 0:
            print('Please enter a number greater than 0.')
            continue

...     except ValueError:
...         print('Please enter a whole number.')
...         continue
... 
...     total_drinks += amount
... 
...     # Simplified game BAC calculation
...     # 3 beers = 0.05 BAC
...     ba += (alcohol * amount) * (0.05 / (1.4 * 3))
... 
...     print()
...     print(f'You drank {amount} x {drink}.')
...     print(f'Total drinks: {total_drinks}')
...     print(f'Estimated BAC: {ba:.3f}')
... 
... 
... print()
... print('--------------------------------')
... print('GAME SUMMARY')
... print('--------------------------------')
... print(f'Total drinks: {total_drinks}')
... print(f'Estimated BAC: {ba:.3f}')
... print('The game is now calculating the consequences...')
... 
... if ba >= 1:
...     print('GODDAM, your dead. At this stage there would be more than a kilo of alcohol in your blood stream!')
... 
... elif ba >= 0.2:
...     print('At over 0.2 BAC, you are either about to pass out, or black out.')
... 
... elif ba >= 0.1:
...     print('At over 0.1 BAC, you are struggling to speak, have a loss of motor skills and inhibitions.')
... 
... elif ba >= 0.05:
...     print('Your estimated BAC is 0.05 or higher. Driving in this state is illegal.')
...   

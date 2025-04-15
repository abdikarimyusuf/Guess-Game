import random

choices = ['r','p','s']

emojis = {'r':'🪨','p':'🔖','s':'✂'}
while True:

    user_choice= input("rock,paper or sciccors? (r/p/s):" ).lower()
    if user_choice not in choices:
     print ('invalid input')
     continue

    computer_choice=random.choice(choices)

    print (f'you chose:{emojis[user_choice]}')
    print (f'computer chose:{emojis[computer_choice]}')


    if user_choice == computer_choice:
        print('tie')

    elif user_choice == 'r' and computer_choice == 'p':
        print('computer won')
    elif user_choice == 'p' and computer_choice == 'r':
        print('you won')
    elif user_choice == 's' and computer_choice == 'p':
        print('you won')
    elif user_choice == 'p' and computer_choice == 's':
        print('computer won')
    elif user_choice == 's' and computer_choice == 'r':
        print('computer won')
    elif user_choice == 'r' and computer_choice == 's':
        print('you won')

    should_continue=input('do you want to continue: (y/n):').lower()
    if should_continue =='n':
        break
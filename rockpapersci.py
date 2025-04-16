import random

choices = ['r','p','s']

emojis = {'r':'🪨','p':'🔖','s':'✂'}
def user_choice():
  while True:
    user_choice= input("rock,paper or sciccors? (r/p/s):" ).lower()
    if user_choice in choices:
        return user_choice
    else:
        print ("invalid input")
        continue

    
def user_display(user_choce,computer_choice):
        print (f'you chose:{emojis[user_choce]}')
        print (f'computer chose:{emojis[computer_choice]}')

def determine_winner(user_choice,computer_choice):
   
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
        

        
       

def play_game():       
    while True:

        player=user_choice()

            

        computer_choice=random.choice(choices)
        
        user_display(player,computer_choice)

        determine_winner(player,computer_choice)


        should_continue=input('do you want to continue: (y/n):').lower()
        if should_continue =='n':
                break
            

play_game()
        

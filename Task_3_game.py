import random

def game_rules(user_choice, computer_choice):

    if (user_choice == computer_choice):
        return "It's a draw!"
    
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissor' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    
    else: 
        return "You lose!"
    
    
def main():

    user_score = 0
    computer_score = 0

    choices = ['rock', 'paper', 'scissors', 'quit']

    print("Let's play Rock, Paper, Scissors!")
    print("\nGame Guide")
    print("If you want to quit, type 'quit'")
    print("Enter one of the 3 choices: 'Rock', 'Paper', 'Scissors'")
    
    while True: 
        user_choice = input("\nYour choice: ").lower()

        if (user_choice == 'quit'):
            break

        if (user_choice not in choices):
            print("Invalid input! Read the guide and enter the correct choice")

        else:
            result = game_rules

        computer_choice = random.choice(choices)

        print("Your choice is: ", user_choice)
        print("Computer's choice is: ", computer_choice)

        result = game_rules(user_choice, computer_choice)
        print(result)

        if (result == "You win!"):
            user_score += 1
        elif (result == "You lose!"):
            computer_score += 1

        print("\nYour score: ", user_score, "\nComputer's score: ", computer_score)   

if __name__ == "__main__":
    main()

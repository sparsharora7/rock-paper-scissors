import random


def get_user_choice():
    while True:
        user_choice = input(" Choose Rock , paper , scissors ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print('Invalid choice')


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie"
    elif (
            (user_choice == 'rock' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'rock')):

        return "you lose"
    else:
        return "you win"


def play_game():
    print("Lets play rock paper scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("you chose", user_choice)
        print("computer chose", computer_choice)

        result = determine_winner(user_choice, computer_choice)

        print(result)
        play_again = input("Do you want to play again? Y or N").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    play_game()



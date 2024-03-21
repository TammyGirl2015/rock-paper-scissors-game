import random

"""
Initialize scores
"""
player_score = 0
computer_score = 0

"""
Welcome message and instructions on how to play.
"""
print("Welcome to rock(🪨 ) -paper(🗒 )-scissors(✂ ). To play, enter one of the three choices in lowercase when prompted. \n Rock smashes scissors, scissors cuts paper and paper covers rock. \nThe game is best out of three. \nGood luck!")

while player_score < 2 and computer_score < 2:
    """
    Main game loop: player is prompted to enter an option and computer chooses a random option. 
    """
    computer = random.choice(['rock', 'paper', 'scissors'])
    
    while True:
        """
        Input validation: keep asking for input until a valid choice is made.
        """
        player = input("Enter your move (rock, paper, scissors): ").lower()
        if player in ['rock', 'paper', 'scissors']:
            break
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

    """
    This code determines the winner of the round as per the game rules by displaying '1' for the winner, '0' for the loser and 'tie' if it is a draw.
    """
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

"""
This code determines the final winner of three rounds and displays the player or computer as the winner or a tie if it is a draw.
"""
if player_score == 2:
    print("Congratulations, you win the series!")
elif computer_score == 2:
    print("Computer wins the series!")
else:
    print("The series is a draw!")


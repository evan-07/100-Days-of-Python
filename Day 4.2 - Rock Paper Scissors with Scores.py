rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_score = 0
computer_score = 0


def game(player_score, computer_score):

    while True:
        try:
            player = int(
                input(
                    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
                ))
            if player < 0 or player > 2:
                raise ValueError  #this will send it to the print message and back to the input option
            break
        except ValueError:
            print("Invalid integer. The number must be in the range of 0-2.")

    # Store the ascii string on a list to be used as reference using an index
    choices = [rock, paper, scissors]
    # Display the player's choice using the list of ascii characters
    print("You chose:\n")
    print(choices[player])

    # Generate a random integer from 0-2 which represents the computer's hand
    computer = random.randint(0, 2)
    print("Computer chose:\n")
    print(choices[computer])
    # Player chooses Rock
    if player == 0 and computer == 1:
        print("You lose!")
        computer_score += 1
    elif player == 0 and computer == 2:
        print("You win!")
        player_score += 1
    # Player chooses Paper
    elif player == 1 and computer == 0:
        print("You win!")
        player_score += 1
    elif player == 1 and computer == 2:
        print("You lose!")
        computer_score += 1
    # Player chooses Scissors
    elif player == 2 and computer == 0:
        print("You lose!")
        computer_score += 1
    elif player == 2 and computer == 1:
        print("You win!")
        player_score += 1
    else:
        print("It's a tie!")

    print("Current score:")
    print(f"Player = {player_score}")
    print(f"Computer = {computer_score}")

    return player_score, computer_score


while True:
    try:
        player_score, computer_score = game(player_score, computer_score)
        if player_score == 5 or computer_score == 5:
            break
    except ValueError:
        print("An error occurred during the game.")

print("\n\n\n\n-----Final Score-----")
print(f"Player = {player_score}")
print(f"Computer = {computer_score}")

if player_score == 5:
    print("\n\nCongratulations!!!!!!!!")
else:
    print("\n\nYou can try again.")

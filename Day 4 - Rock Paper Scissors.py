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
if player == 0 and computer == 0:
    print("It's a tie!")
elif player == 0 and computer == 1:
    print("You lose!")
elif player == 0 and computer == 2:
    print("You win!")

# Player chooses Paper
elif player == 1 and computer == 0:
    print("You win!")
elif player == 1 and computer == 1:
    print("It's a tie!")
elif player == 1 and computer == 2:
    print("You lose!")

# Player chooses Scissors
elif player == 2 and computer == 0:
    print("You lose!")
elif player == 2 and computer == 1:
    print("You win!")
else:
    print("It's a tie!")

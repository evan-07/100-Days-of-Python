from art import logo, vs
from game_data import data
import random

# Print logo
print(logo)

is_first_run = True
is_continue = True
data_A = ''
data_B = ''
score = 0

def generate_data():
    data_A = random.choice(data) 
    new_data = [el for el in data if el != data_A]
    data_B = random.choice(new_data)
    return data_A, data_B


while is_continue:
    if is_first_run:
        data_A, data_B = generate_data()
        is_first_run = False

    print(f"Compare A: {data_A['name']}, {data_A['description']}, from {data_A['country']}")
    print(vs)
    print(f"Against B: {data_B['name']}, {data_B['description']}, from {data_B['country']}")

    print(data_A['follower_count'])
    print(data_B['follower_count'])

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if answer == 'a':
        if data_A['follower_count'] > data_B['follower_count'] :
            new_data = [el for el in data if el != data_A]
            data_B = random.choice(new_data)
            is_continue = True
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            is_continue = False
    if answer == 'b':
        if data_B['follower_count'] > data_A['follower_count'] :
            data_A, data_B = generate_data()
            is_continue = True
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            is_continue = False







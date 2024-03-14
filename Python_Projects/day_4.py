import random

def computer():
    computer_choice = random.choice(["Rock","Paper","Scissors"])
    print(computer_choice)
    return computer_choice.lower()

print("Lets play rock paper and scissors")
user = input("Your Turn \n")

if user == computer():
    print("Draw")
elif (user == 'rock' and computer() == 'scissors') or \
     (user == 'paper' and computer() == 'rock') or \
     (user == 'scissors' and computer() == 'paper') :
    print('User wins')
else:
    print('Computer wins')



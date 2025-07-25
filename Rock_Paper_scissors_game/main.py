import random
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
game = [rock,paper,scissors]
function = True
while function:
    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
    if user >= 3 or user < 0:
        print("Invalid Input")
    else:
        print(game[user])
        computer = random.randint(0,2)
        print("VS")
        print(game[computer])

        if computer > user:
            print("You loose")
        elif user == computer:
            print("It's Draw")
        elif user == 2 and computer == 0:
            print("You loose")
        elif user == 0 and computer == 2:
            print("You Win")
        elif user > computer:
            print("You Win")
    still_play = input("Do you want to play again:\n")
    if still_play == "no":
        function = False
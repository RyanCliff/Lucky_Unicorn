# Import random
import random

# Functions
def yes_no(question):
    valid = False
    while not valid:
        answer = input(question).lower()
        if answer == "yes" or answer == "y":
            print("start game")
            return answer
        elif answer == "no" or answer == "n":
            print("display instructions")
            return answer
        else:
            print("Please pick yes or no.")

def instructions():
    print("***How To Play***")
    print()
    print("The rules of the game are.")
    print()
    return ""

def num_check(question, low, high):
      error = "Please enter a whole number between 1 and 10"
      valid = False
      while not valid:
          try:
            response = int(input(question))

            if low < response <= high:
                return response
            else:
                print(error)
          except ValueError:
              print(error)

# Main Routine
print("Welcome to the Lucky Unicorn Game!!")
show_instructions = yes_no("Have you played the Lucky Unicorn game before? ")
if show_instructions == "yes":
    instructions()
    print()

print()

how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))

balance = how_much

rounds_played = 0

play_again = input("Press <ENTER> to play....").lower()
while play_again == "":
    rounds_played += 1
    print()
    print("*** Round #{} ***".format(rounds_played))
    chosen_num = random.randint(1, 100)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            balance -= 0.5
        else:
            chosen = "zebra"
            balance -= 0.5
    print("You got a {} your balance is ${:.2f}".format(chosen, balance))
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry, you have run out of money")
    else:
        play_again = input("Press enter to play again or 'xxx' to quit.")

print("Balance: ${:.2f}".format(balance))

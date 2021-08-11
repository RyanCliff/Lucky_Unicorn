import random

tokens = ["unicorn", "horse", "horse", "horse", "zebra", "zebra", "zebra", "donkey", "donkey", "donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE
for item in range(0,500):
    chosen = random.choice(tokens)

    if chosen == "unicorn":
        balance += 4
        print(balance)
    elif chosen == "horse" or chosen == "zebra":
        balance -= 0.5
        print(balance)
    else:
        balance -= 1
        print(balance)

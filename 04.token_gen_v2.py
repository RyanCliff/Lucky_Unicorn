import random

tokens = ["unicorn", "horse", "zebra", "donkey"]
balance = 100

for item in range(0,20):
    chosen = random.choice(tokens)

    if chosen == "unicorn":
        balance += 4
    elif chosen == "horse" or chosen == "zebra":
        balance -= 0.5
    else:
        balance -= 1

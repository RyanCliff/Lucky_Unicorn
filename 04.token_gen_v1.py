import random

tokens = ["unicorn", "horse", "zebra", "donkey"]

for item in range(0,20):
    chosen = random.choice(tokens)
    print(chosen)

answer= " "
while answer.lower() != "xxx":
    answer = input("Have you played the Lucky Unicorn game before?").lower()
    if answer == "yes" or answer == "y":
        print("start game")
    elif answer == "no" or answer == "n":
        print("display instructions")
    else:
        print("Please pick yes or no.")

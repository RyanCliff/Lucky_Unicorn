balance = 5

rounds_played = 0

play_again = input("Press <ENTER> to play....")
while play_again == "":
    rounds_played += 1
    print(rounds_played)
    balance -= 1
    print("balance: ", balance)
    print()


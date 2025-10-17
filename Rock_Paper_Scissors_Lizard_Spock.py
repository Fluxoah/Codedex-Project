import os
import random

while True:
    os.system("cls")
    print("================================")
    print("Rock Paper Scissors Lizard Spock")
    print("================================\n")
    print("1) ✊ Rock")
    print("2) ✋ Paper")
    print("3) ✌️ Scissors")
    print("4) 🦎 Lizard")
    print("5) 🖖 Spock")
    
    moves = {
        1: "✊ Rock",
        2: "✋ Paper",
        3: "✌️ Scissors",
        4: "🦎 Lizard",
        5: "🖖 Spock"
    }
    
    bot = random.randint(1, 3)
    p1 = int(input("\n>> "))
    print(f"\nYou chose {moves[p1]}")
    print(f"Bot chose {moves[bot]}\n")
    
    if p1 == bot:
        print("Draw !!")
        choice1 = input("Do you wish to restart or exit ?: ").lower()
        if choice1 == "exit":
            print("Exiting...")
            break
        elif choice1 == "restart":
            print("Restarting...")
            continue
        else:
            print("Invalid Input.")
    elif (p1 == 1 and (bot == 3 or bot == 4)) or \
        (p1 == 2 and (bot == 1 or bot == 5)) or \
        (p1 == 3 and (bot == 2 or bot == 4)) or \
        (p1 == 4 and (bot == 5 or bot == 2)) or \
        (p1 == 5 and (bot == 3 or bot == 1)):
            print("You Won!!")
            choice2 = input("Do you wish to restart or exit ?: ").lower()
            if choice2 == "exit":
                print("Exiting...")
                break
            elif choice2 == "restart":
                print("Restarting...")
                continue
            else:
                print("Invalid Input.")
    else:
        print("Bot Won !!")
        choice3 = input("Do you wish to restart or exit ?: ").lower()
        if choice3 == "exit":
            print("Exiting...")
            break
        elif choice3 == "restart":
            print("Restarting...")
            continue
        else:
            print("Invalid Input.")
import random


def guess():
    r = random.randint(0,10)
    max_number = 10
    total_chances = 10


    while True:
        i = int(input("Guess the number between 0 and 10: "))

        if i > max_number:
            print("You introduced a invalid number, try again!")
            return

        if i == r:
            print("You guessed! Nice!")
            break

        if i >= r:
            print("Try lower!")
            total_chances -= 1
        elif i <= r:
            print("Try higher!")
            total_chances -= 1

        if total_chances == 0:
            print("You have 0 chances! You lost!")
            break

        print(f"You have {total_chances} left!")


guess()
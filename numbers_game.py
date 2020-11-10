from random import randint

answer = randint(0, 10)
count = 0

while count < 3:
    guess = input("Guess a number between 0 and 10: ")
    try:
        if int(guess) == answer:
            print("You got it!")
            break
        else:
            if count == 2:
                print("You lose")
            else:
                print("Try again")
            count += 1
            print(f"You have guessed {count} time(s)")
    except ValueError:
        print("Please enter numbers only.")

print("Game Finished")

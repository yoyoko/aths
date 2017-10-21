#this is a guess the number game
import random
secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")

#ask the player to guess 6 times
for i in range(6):
    print("Take a guess")
    guess = int(input("> "))

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

if guess == secretNumber:
    print(f"Good job! You guessed my number in {i} guesses")
else:
    print(f"No. The number I was thinking of was {secretNumber}")

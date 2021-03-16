import random

print("Welcome to THE Number Guessing Game!")
print("To win, you have to guess the same number as me! You have a 50% chance of winning.")
print("You will have 5 chances. Good Luck!")

number = random.randint(1, 9)

chances = 0

while chances < 5:

    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulation YOU WON!!!")
        break

    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess, ".")

    else:
        print("Your guess was too high: Guess a number lower than", guess, ".")

    chances += 1

if not chances < 5:
    print("YOU LOSE!!! The number is", number)
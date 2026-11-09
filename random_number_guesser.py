import random

first_range = input ("Type in a number: ")

if first_range.isdigit():
    first_range = int(first_range)

    if first_range <= 0:
        print ("Please type in a digit higher than 0")
        quit()

else:
    print ("Please Type in a digit!")
    quit()

random_number = random.randint (0, first_range)
guesses = 0

while True:
    guesses += 1
    guess = input ("Guess a Number: ")

    if guess.isdigit():
        guess = int(guess)

    else:
        print ("Please guess a digit nex time!")
        continue

    if guess == random_number:
        print ("You got it!")
        break

    elif guess > random_number:
        print ("You are above the number!")

    elif guess < random_number:
        print ("You are below the number!")

print ("You got it in", guesses, "guesses")

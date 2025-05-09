import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)

max_attempts = 5
attempts = 0

while attempts < max_attempts:
    attempts += 1
    print("Attempt " + str(attempts) + " of " + str(max_attempts))

    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congrats you won in " + str(attempts)+ " attempts")
        break
    elif guess < secret_number:
        print("too low bro, try again")
    else:
        print("too high gang, again")

if attempts == 5 and guess != secret_number:
    print("so you failed huh?")

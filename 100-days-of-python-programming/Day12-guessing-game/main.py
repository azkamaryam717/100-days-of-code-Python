# random module in Python helps generate random numbers

import random 
# random.randint() generates a random integer between the given values
print(random.randint(1, 100)) # generates a random number between 1 and 100

# Number guessing game in Python

random_number = random.randint(1, 100) 
guess = int(input("Enter your guess(1-100): "))
counter = 1

while guess != random_number:
    if guess < random_number:
        print("Guess Higher!")
    else:
        print("Guess Lower!")
    guess = int(input("Guess again: "))
    counter += 1

print("Congratulations! You guessed right")
print("You took",counter,"attempts to guess the number")
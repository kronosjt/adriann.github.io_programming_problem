# Write a guessing game where the user has to guess a secret number. After every guess the program tells the user
# whether their number was too large or too small. At the end the number of tries needed should be printed.
# I counts only as one try if they input the same number multiple times consecutively.

import random
number = random.randrange(1,10)

previous_guess = int(raw_input("Enter a guess: "))
num_of_guesses = 1

while previous_guess !=  number:
    if previous_guess < number:
        num_of_guesses += 1
        print "Guess is less than secret number. Try again"
        new_guess = int(raw_input("Enter a new guess:"))
    else:
        num_of_guesses += 1
        print "Guess is larger than secret number. Try again"
        new_guess = int(raw_input("Enter a new guess:"))
    if new_guess == previous_guess: # if user inputs same number consecutively
        num_of_guesses -= 1 # reduce the guess count
    previous_guess = new_guess
else:
    print "Congrats! You guessed the correct number in %d tries" % num_of_guesses
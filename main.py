# import the function random to generate numbers
import random

# define variable x to contain the number
x = random.randint(1, 10)

# define the counter of the loop
c = 0

# Take the name of the player
name = input("Hello, What's your name?\n")

# print the hello statement
print("okay! " + name + " I'm guessing a number between 1 and 10:\n")

while c < 5:
    # take the input from the user
    z = int(input())

    if z > x:
        print("Your guess is too high:\n")
    elif z < x:
        print("Your guess is too low:\n")
    else:
        break
    c += 1  # increase the loop counter

# if he got the number in less than 5 tries he wins and receive number of tries
if c < 5:
    print("You guessed the number in ", c, "tries!")
else:
    print("Sorry you have lose!")

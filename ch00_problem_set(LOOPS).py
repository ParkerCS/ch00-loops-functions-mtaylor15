# LOOPS (22pts TOTAL)
import math
import random

# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.
number = 1
next_number = 2
last_number = 0

while next_number < 1000:
    number = last_number + number
    next_number = number
    last_number = next_number
    print(next_number)




# PROBLEM 2 (Number Guessing Game - 6pts)
# Write a program that takes a random integer between 1 and 1000
# The program then asks the user to guess the number.
# After every guess, the program will say either “Lower”
# if the number it took is lower, “Higher” if the number it took is higher,
# and “You guessed it!” if the number it took is equal to the number
# It might be wise, for testing purposes, to also display the number that the
# program randomly picks, until you are sure that the program works correctly
number_range = random.randrange(1, 1001)

user_input = input("Guess the number I am thinking of between 1 and 1000: ")

if user_input > 1000:
    print("You cant guess that number")
if user_input > number:
    print("You guess is too low. DO BETTER ")

if user_input < number:
    print("Why would even guess a number that high? ")

if user_input == number:
    print("Its about time you got it")


# PROBLEM 3 (Dice Hi-Low - 6pts)
# You roll five six-sided dice, one by one.
# How big is the probability that the value of each die
# is greater than or equal to the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.



# PROBLEM 4 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.

for a in range(1, 11):
    for b in range(11):
        for c in range(11):
            for d in range(1, 11):
                if int(str(d)+str(c) + str(b) + str(a)) == (int(str(a) + str(b) + str(c) + str(d))**4):
                    print(a, b, c, d)


#SECTION 2 - FUNCTIONS (20PTS TOTAL)
import math
import random

#PROBLEM 1 (Length of String - 3pts)
# Make a function which asks the user to enter a string, then prints the length of that string.
# You will need to use the input() function.
# Make a call to that function

def length(string_number):
    str(string_number)
    print("It is", len(string_number))

user_input= input("Pick a number: ")



# PROBLEM 2 (Pythagorean theorem - 4pts)
# The Pythagorean theorem states that of a right triangle, the square of the
# length of the diagonal side is equal to the sum of the squares of the lengths
# of the other two sides (or a^2 + b^2 = c^2).
# Write a program that asks the user for the lengths of the two sides that meet at a right angle.
# Then calculate the length of the third side, and display it in a nicely formatted way.
# You may ignore the fact that the user can enter negative or zero lengths for the sides.
def pythagorean():
    a = input("Put in one side of a triangle: ")
    b = input("Put in another side of a triangle: ")
    c = ((int(b**2) + (int(a)**2))**.5)
    print("The other side is: ", c)
pythagorean()
print()



# PROBLEM 3 (Biggest, smallest, average - 4pts)
# Make a function to ask the user to enter three numbers.
# Then print the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.
# Make a call to your function.
def stuff():
    num1 = input("put in a number:")
    num2 = input("put in a number:")
    num3 = input("put in a number:")
    if num1 > num2 and num1 > num3:
        print(num1, "is the largest")
    if num2 > num3 and num2 > num1:
        print(num2, "is the largest")
    if cnum3> num2 and num3 > num1:
        print(num3, "is the largest")
    if num2 < num3 and num2 < num1:
        print(num2, "is the smallest")
    if num3 < num2 and num3 < num1:
        print(num3, "is the smallest")
    average = round(((num1 + num2 + num3 )/ 3), 1)
    print("Average =", average )
stuff()
print()

# PROBLEM 4 (e to the... - 3pts)
# Calculate the value of e (from the math library) to the power of -1, 0, 1, 2, and 3.
# display the results, with 5 decimals, in a nicely formatted manner.

# PROBLEM 5 (Random int - 3pts)
# Generate a random integer between 1 and 10 (1 and 10 both included),
# but only use the random() function (randrange is not allowed here)
number = float(random.random()*11)
print(number)

# PROBLEM 6 (add me, multiply me - 3pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.
user = input("pick a number: ")
user2 = input("pick another number: ")

sum = user + user2
print("The sum is: ", sum)

product = user * user2
print("The product is: ", product)

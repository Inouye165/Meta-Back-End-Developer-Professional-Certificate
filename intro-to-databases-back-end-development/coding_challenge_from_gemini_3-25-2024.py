# Challenge 1: Even or Odd

# Task: Create a program that takes a number as input and determines if it's even or odd.
# How:
# Use the modulo operator (%) to get the remainder when dividing by 2.
# If the remainder is 0, it's even; otherwise, it's odd.
# Challenge 2:  FizzBuzz

# Task: Write a program that prints numbers from 1 to 100, but with a twist:
# For multiples of 3, print "Fizz".
# For multiples of 5, print "Buzz".
# For multiples of both 3 and 5, print "FizzBuzz".
# How:
# Use a loop to iterate through the numbers.
# Inside the loop, use conditional statements (if, elif, else) to check for divisibility and print the appropriate word.
# Challenge 3: Reverse a String

# Task: Take a string as input and print it in reverse order.

number = int(input("Enter an integer:"))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
string = input("Enter a string:")
print(string[::-1])
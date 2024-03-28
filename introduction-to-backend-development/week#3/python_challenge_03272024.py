# Create a Python script that calculates the factorial of a number. The factorial of a number 
# n is the product of all positive integers less than or equal to n. For example, the factorial of 5 (denoted as 5!) is 5 x 4 x 3 x 2 x 1 = 120.

# Requirements:
# Your script should define a function called factorial that takes a single argument n.
# The function should return the factorial of n.
# Ensure your script works for n = 0 (the factorial of 0 is 1).
# After defining the function, make your script prompt the user to enter a number and then print the factorial of that number.
# This challenge tests your ability to implement mathematical concepts in Python, handle user input, and perform basic error checking.


def factorial(n):
    assert isinstance(n, int) and n >= 0, "The input must be a non-negative integer"
    n_factored = 1
    for x in range(1, n+1):
        n_factored = n_factored * x
    return n_factored
try:
    user_number = input('Enter an integer: ')
    user_number = int(user_number)
except:
    print('Enter a valid integer,')
assert factorial(0) == 1, "The factorial of 0 should be 1"
assert factorial(1) == 1, "The factorial of 1 should be 1"
assert factorial(5) == 120, "The factorial of 5 should be 120"
print('Your number factored is', factorial(user_number))


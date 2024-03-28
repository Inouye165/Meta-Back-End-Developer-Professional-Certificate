num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
string = ""
while string == "":
    string = input("Enter a '+-/*': ")
    if string == "+":
        print(int(num1) + int(num2))
    elif string == "-":
        print(int(num1) - int(num2))
    elif string == "*":
        print(int(num1) * int(num2))
    elif string == "/":
        print(int(num1) / int(num2))
    elif string == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid operator")
        string = ""
        
# Compare this snippet from coding_challenge_from_gemini_3-25-2024.py:

def fizzbuzz():
    """Prints the FizzBuzz sequence with the 'Boom' twist."""
    for num in range(1, 51):
        output = ""
        if num % 15 == 0:
            output += "FizzBuzz"
        elif num % 3 == 0:
            output += "Fizz"
        elif num % 5 == 0:
            output += "Buzz"
        elif "7" in str(num):
            output += "Boom"
        else:
            output = str(num)  # Convert to string for consistent output
        print(output)


def is_palindrome(word):
    """Checks if a given word is a palindrome."""
    return word == word[::-1]


def simple_calculator():
    """Performs basic calculations."""
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            operator = input("Enter an operator (+, -, *, /, exit): ")
            if operator == "+":
                print(num1 + num2)
            elif operator == "-":
                print(num1 - num2)
            elif operator == "*":
                print(num1 * num2)
            elif operator == "/":
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    print(num1 / num2)
            elif operator == "exit":
                print("Goodbye!")
                break
            else:
                print("Invalid operator")
        except ValueError:
            print("Invalid number input. Please try again.")


# Example usage
if __name__ == "__main__":
    fizzbuzz()

    user_word = input("Enter a word to check for palindrome: ")
    if is_palindrome(user_word):
        print("Palindrome!")
    else:
        print("Not a palindrome.")

    simple_calculator()

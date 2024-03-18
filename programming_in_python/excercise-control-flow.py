# List of numbers to work with
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11,45]
count = 0

# Enumerating through num_list to compare each number against 45
for i, num in enumerate(num_list):
    if num > 45:
        print(num,' is greater than 45')
    elif num == 45:
        print(num, ' is equal to 45')
    else:
        print(num, ' is less than 45')
    count += 1

# Print a line break and summary of the first example
print("\n---\nThis section demonstrates iterating over a list with enumerate, comparing each item against the number 45, and counting iterations.\n---\n")

# List of colors to iterate through
colors = ['red', 'green', 'blue']

# Enumerating through colors list and printing each color with its index
for index, color in enumerate(colors):
    print(f"Color at index {index}: {color}")

# Print a line break and summary of the second example
print("\n---\nThis section shows how to use enumerate to get both the index and the value while iterating over a list of colors.\n---\n")

# List of numbers for modification
numbers = [10, 20, 30, 40]

# Doubling the value of even numbers in the list
for index, num in enumerate(numbers):
    if num % 2 == 0:  # Check for even numbers
        numbers[index] = num * 2  # Double the value

# Printing the modified list
print(numbers)

# Print a line break and summary of the third example
print("\n---\nThis section demonstrates modifying a list in place, specifically doubling the value of even numbers.\n---\n")

# Lists of teams and their rankings
teams = ["Lakers", "Warriors", "Celtics"]
ranking = [1, 2, 3]

# Creating a dictionary from two lists using enumerate for ranking
team_standings = {team: rank for rank, team in enumerate(teams, start=1)}
print(team_standings)

# Print a line break and summary of the fourth example
print("\n---\nThis final section shows how to create a dictionary from a list using enumerate to assign rankings to each team.\n---\n")

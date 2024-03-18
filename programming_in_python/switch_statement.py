def switch_example1(argument):
    switch = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three"
    }
    return switch.get(argument, "Invalid input")

def if_then_example1(argument):
    if argument == 0:
        return "Zero"
    elif argument == 1:
        return "One"
    elif argument == 2:
        return "Two"
    elif argument == 3:
        return "Three"
    else:
        return "Invalid input"

# Function calls
result1 = switch_example1(2)
print("Result of switch_example1(2) is:", result1)

result2 = if_then_example1(1)
print("Result of if_then_example1(1) is:", result2)
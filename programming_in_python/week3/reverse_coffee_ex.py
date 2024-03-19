
coffee_types = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha", "Macchiato", "Flat White", "Affogato", "Turkish Coffee", "Irish Coffee"]
def reverse_coffee(coffee_types):
    return coffee_types[::-1]   
reverse_coffee = list(map(reverse_coffee, coffee_types))
for x in reverse_coffee:
    print('with map',x)
    
    
coffee_types = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha", "Macchiato", "Flat White", "Affogato", "Turkish Coffee", "Irish Coffee"]

reversed_coffee = [coffee[::-1] for coffee in coffee_types]

for x in reversed_coffee:
    print('with list comp',x)


coffee_types = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha", "Macchiato", "Flat White", "Affogato", "Turkish Coffee", "Irish Coffee"]


# Reverse the spelling of each element while also reversing the list
for i in range(len(coffee_types) // 2):
    coffee_types[i], coffee_types[-i - 1] = coffee_types[-i - 1][::-1], coffee_types[i][::-1] 

# Print the reversed list
for x in coffee_types:
    print('3rd',x)

coffee_types = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha", "Macchiato", "Flat White", "Affogato", "Turkish Coffee", "Irish Coffee"]

for word in coffee_types:
    print('easiest',word[::-1])   
    
# finally the shortest way to reverse a list
print(*map(lambda w:w[::-1], ["hello", "world", "coding"]),sep="\n")
print(*map(lambda w:w[::-1], coffee_types),sep="\n")
#chatGPT found a shorter way to reverse a list of strings.
print("\n".join([w[::-1] for w in coffee_types]))

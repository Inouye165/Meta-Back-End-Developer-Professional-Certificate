# Video from https://www.coursera.org/learn/programming-in-python/lecture/ynhJp/map-filter

menu = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha", "Macchiato", "Flat White", "Affogato", "Turkish Coffee", "Irish Coffee"]
def find_coffee(coffee):
    if coffee[0] == "C":
        return coffee
    
map_coffee = map(find_coffee, menu)
print(map_coffee)
for x in map_coffee:
    print(x)
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)    

# CoPilot: Python Map and Filter Functions
menu = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha", "Macchiato", "Flat White", "Affogato", "Turkish Coffee", "Irish Coffee"]
def find_coffee(menu):
    return list(filter(lambda x: 'Coffee' in x, menu))
print(find_coffee(menu))
# # Excercise from map and filter video
# menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

# def find_coffee(coffee):
#     if coffee[0] == 'c':
#         return coffee

# map_coffee = map(find_coffee, menu) # This will return a map object
# print(map_coffee) # This will print the map object
# for x in map_coffee: # This will print the items in the map object and consume it
#     print(x)
# print(map_coffee) This map object is now empty
# print(list(map_coffee)) # This will print an empty list because map_coffee is now empty
def sum(n):
    print(n)
    if n == 1:
        return 0
    return n + sum(n-1)

a = sum(5)
print(a)



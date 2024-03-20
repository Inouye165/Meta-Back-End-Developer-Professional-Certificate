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
# def sum(n):
#     print(n)
#     if n == 1:
#         return 0
#     return n + sum(n-1)

# a = sum(5)
# print(a)
class Animal:
	def __init__(self, name, species, age)->None:
		self.name = name
		self.species = species
		self.age = age
    def make_sound(self) -> None:
        print('grr')

class Mammal(Animal):
    def __init__(self, name, species, age, num_legs):
        self.name = name
        self.species = species
        self.age = age
        self.num_legs = num_legs
    def make_sound(self):
        print('Bark')
		

class Bird(Animal):
    def __init__(self, name, species, age, wingspan):
        self.name = name
        self.species = species
        self.age = age
        self.wingspan = wingspan
    def make_sound(self):
        print('tweet')

animal = Animal('Rex', 'Dog', 5)
dog = Mammal('dobby', 'dog', 3, 4)
parrot = Bird('tweety', 'parrot', 2, 5)

animal.make_sound()
dog.make_sound()
parrot.make_sound()


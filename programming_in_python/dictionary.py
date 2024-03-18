# Create a dictionary with index numbers and names
people = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
    4: "David",
    5: "Eve",
    6: "Frank",
    7: "Grace",
    8: "Henry",
    9: "Ivy",
    10: "Jack"
}
# for key, value in people.items():
#     print(key, value)

# for key in people.keys():
#     print(key)

for value in people.values():
    print(value)
print(people[5])  # Prints the name of the person with index 5
if 6 in people:
    print(people[6])
else:
    print("Key not found.")
people[11] = 'Kyle'
people[1] = 'Alicia'  # Changes 'Alice' to 'Alicia'

for key, value in people.items():
    if value.startswith('A'):
        print(key, value)
long_names = {key: value for key, value in people.items() if len(value) > 4}
print(long_names)

people_names = [name for name in people.values()]
print(people_names)
for name in people_names:
    print(name)
for key, value in people.items():
    # print('key',key, 'value',value)
    # print(f'key {key} value {value}')
    print("key {} value {}".format(key, value))
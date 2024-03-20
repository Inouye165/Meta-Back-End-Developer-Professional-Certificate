
# List Comprehension Challenge: Create a new list containing only the lowercase words from the words list.

words = ["Apple", "banana", "Cherry", "lemon", "Mango"]
# list = [word.lower() for word in words]
# lowercase_words = [word for word in words if word.islower()]
# print(list)
# print(lowercase_words)

# Dictionary Comprehension: Challenge: Create a dictionary where the keys are the words from the words list and the values are the lengths of those words.

# list_dict = {word:len(word) for word in words}
# print(list_dict)
# Challenge: Create a set containing the unique first letters (all lowercase) of the words in the words list.

# list_set = {word[0].lower() for word in words}
# print(list_set)

# list_generator = ((x*2)**2 for x in range(10))
# print(list_generator)
# print(list(list_generator))

# squares = (number**2 for number in range(20) if number % 2 == 0)

# # Print the first five squares using a loop:
# for i in range(5):
#    print(next(squares))

a = [[96], [69]]

print(''.join(list(map(str, a))))
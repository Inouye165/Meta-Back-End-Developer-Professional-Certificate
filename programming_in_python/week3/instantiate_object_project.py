# class MyFirstClass():
#     def __init__(self):
#         print("Who wrote this?")
#         index = "Author-Book"

#     def hand_list(self, philosopher, book):
#         print(f"{philosopher} wrote the book: {book}")
        
# MyFirstClass().hand_list("Sun Tzu", "The Art of War")


# # Sample Solution code exemplar.  Prints things twice so I dont know that it is correct.

# class MyFirstClass():
#     print("Who wrote this?")
#     index = "Author-Book"

#     def hand_list(self, philosopher, book):
#         print(MyFirstClass.index)
#         print(philosopher + " wrote the book: " + book)

# whodunnit = MyFirstClass()
# whodunnit.hand_list("Sun Tzu", "The Art of War")

class MyFirstClass():
    print("Who wrote this?")
    index = "Author-Book"
    def hand_list(self, philosopher, book, year):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book + " in the year " + year)
whodunnit = MyFirstClass()
whodunnit.hand_list("Sun Tzu", "The Art of War","1300")
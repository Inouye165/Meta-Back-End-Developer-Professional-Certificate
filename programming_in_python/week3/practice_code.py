# num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# def find_odd(list):
#     if list % 2 == 1:
#         return list
#     return None

# map1 = map(find_odd, num_list)
# print(map1)
# for x in map1:
# 	print(x)
 
# list1 = list(map1)
# print(list1)
# for x in list1:
# 	print('list: ',x)

# class Book:

#     def __init__(self, title, author, quantity):

#             self.title = title
#             self.author = author
#             self.quantity = quantity


#     def add_stock(self, quantity):
#         self.quantity += quantity

#     def sell_book(self):
#         if self.quantity < 1:
#             print('Out of stock')
#         else:
#             self.quantity -= 1
#             print('Sold, ',self.quantity, ' remaining')
		

# LOR = Book("Lord of the Rings", "JRR Tolkien", 5)
# hobbit = Book("The Hobbit", "JRR Tolkien", 7)

# LOR.add_stock(5)
# LOR.sell_book()

class Book:
	def __init__(self, title, author, quantity):
		self.title = title
		self.author = author
		self.quantity = quantity


	def add_stock(self, quantity):
		self.quantity += quantity
		print("Stock is ",self.quantity)

	def sell(self):
		if self.quantity < 1:
			print('Out of stock')
		else:
			self.quantity -= 1
			print('Stock is now ',self.quantity)

LOR = Book("LOR", "JRR", 10)

LOR.sell()
LOR.add_stock(10)
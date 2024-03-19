# with open('test.txt', 'r') as file:
#     print(file.readlines())
# I thought the code below would cause problems because the file is not closed. However, it worked fine. I think the file is closed automatically after the block is executed.
# however the code does not show an apparent error, 
# it is better to use the code above to close the file properly.
# file = open('test.txt', 'r')
# print(file.readline())

# f = open('test.txt', 'r')
# print(f.readline())
# f.close()

# with open('test.txt','r') as f:
# 	doc = .readlines()
# for line in doc:
# 	print(line)

# try:
#     with open('test1.txt','r') as file:
#         doc =  file.readlines()
#         print('pass')
# except FileNotFoundError as e:
#     print('super duper error:', e)
	
# try:
#     with open('test.txt', 'r') as file:
#         # print(file.readlines(3)) This did not work as intended
#         print([line for line in file.readlines()[:3]])# List Comprehension by Copilot
# except FileNotFoundError as e:
#     print("Error ---- ", e)
# import random
# f_name= input('Enter file name: ')
# try :
#     with open( f_name, 'r') as file:
#         f_contents = file.read()
# except FileNotFoundError as e:
#     print('Error:', e)
# print(f_contents)
# f_contents_list = f_contents.split('\n')
print(f_contents_list)
print(random.choice(f_contents_list)) # random.choice() returns a random element from the non-empty sequence.
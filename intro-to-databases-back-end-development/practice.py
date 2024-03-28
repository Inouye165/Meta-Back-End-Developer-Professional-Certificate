string = input("Enter a string: ")
# open a file in write mode
with open("output.txt", "w") as file:
	# write the string to the file
	file.write(string)
 # list files in the current directory
import os
print(os.listdir())
with open("output.txt", "r") as file:
	# read the file contents
	print(file.read())
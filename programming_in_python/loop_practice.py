# print('Print Even Numbers: Write a for loop to print all even numbers between 1 and 20 (inclusive).')
# for count in range(1, 21):
#     if count % 2 == 0:
#         print(count)
# print("Reverse a String:  Use a for loop to print the characters of a string in reverse order.")        
# string = 'Dobby'
# reverse = ''
# for count in range(len(string)):
#     reverse = reverse + string[len(string)-count-1]
# print('looping over in reverse =',reverse)
# print('string[::-1] =', string[::-1])
print('FizzBuzz: Create a for loop to print the numbers 1 to 100. For multiples of 3, print "Fizz". For multiples of 5, print "Buzz". For multiples of both 3 and 5, print "FizzBuzz"')
for count in range(100):
	if count % 3 == 0 and count % 5 == 0:
		print(count, 'FizzBuzz')
	elif count % 3 == 0:
		print(count, 'Fizz')
	elif count % 5 == 0:
		print(count, 'Buzz')
	else:
		print(count)
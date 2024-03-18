# The below code was the example given in the lecture. It is not correct.

# def isPalindrome(str):
#     startIndex = 0
#     endIndex = len(str) - 1

#     for x in str:
#         if str[startIndex] != str[endIndex]:
#             return False

#     return True

# print(isPalindrome('racecars'))

# This is the correct code. Notice the difference in the algorithm.   statement.
# The first code is incorrect because it only checks the first and last character
# of the string. The second code checks the first and last character, then the second
# and second to last character, and so on. It is a more complete algorithm.
def isPalidrome(str):
    startIndex = 0
    endIndex = len(str) - 1
    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
        startIndex += 1
        endIndex -= 1
    return True
print(isPalidrome("racecar")) # True
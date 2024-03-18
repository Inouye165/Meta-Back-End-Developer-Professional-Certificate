def string_reverse(str):
    print(str)
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0] 
    
str = "reversal"
reverse = string_reverse(str)
print("The original string is: ", str)
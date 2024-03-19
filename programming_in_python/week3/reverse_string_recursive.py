# I changed the parameter name in the function to
# avoid variable shadowing with the variable in the
# main code. This ensures clarity about which 
# variable we're working with at different points.
# and the main section
def string_reverse(Function_string):
    print(original_string)
    print(Function_string)
    if len(Function_string) == 0:
        return Function_string
    else:
        return string_reverse(Function_string[1:]) + Function_string[0] 
    
original_string = "reversal"
reverse = string_reverse(original_string)
print("The original string is: ", original_string)
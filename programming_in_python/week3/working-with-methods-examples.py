# # Example 1
# class A:
#    def a(self):
#        return "Function inside A"

# class B:
#     def a(self):
#         return "Function inside B"

# class C(B,A):
#     pass

# # Driver code : Driver code is the code that calls the function
# c = C()
# print(c.a()) #output is" Function inside B" as it is first class in the list of classes inherited

# Example 2
# class A:
#     def b(self):
#         return "Function inside A"

# class B:
#     def b(self):
#         return "Function inside B"

# class C(A, B):
#     def b(self): # if this method is not present then it will call the first class method and the final print will be "Function inside A"
#         return "Function inside C"
#     pass

# class D(C):
#     pass
# example = 2
# d = D() #Driver code
# print(d.b()) #output is "Function inside C" as it is first class in the list of classes inherited

# Example 3
# class A:
#     def c(self):
#         return "Function inside A"

# class B:
#     def c(self):
#         return "Function inside B"

# class C(A, B):
#     def c(self):
#         return "Function inside C"

# class D(A, C):
#     pass

# d = D()
# print(d.a)  # Output is "Cannot create a consistent method resolution" as it is not possible
#             # to create a consistent method resolution order for the classes A, C, D

# Example 4
class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())    # Output is "Function inside E" as it is first class in the list of classes inherited
print(F.mro())  # Output is "[<class '__main__.F'>, <class '__main__.E'>, <class '__main__.D'>, 
                # <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
                
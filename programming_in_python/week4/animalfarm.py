def d():
    animal = "elephant" #This is a local variable
    def e():
        nonlocal animal # This is a nonlocal variable
        animal = "giraffe" # This is a nonlocal variable
        print("Inside nested functon: " + animal)
    print("Before calling nested function: " + animal)
    e()
    print("After calling nested function: " + animal)
animal = "camel" # This is a global variable
d()
print("Global animal: " + animal)

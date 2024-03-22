def d():
    color = "green"
    def e():
        nonlocal color #this is the key line 
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"
color = "blue"
d()
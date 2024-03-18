list = [1,2,3,4,5,6,7,8,9,10]
def add_to_list(list):
    new_list = list.copy()
    new_list.append(11)
    return new_list

new_list = add_to_list(list)
print(list)
print(new_list)

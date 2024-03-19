num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

def find_odd(list):
    if list % 2 == 1:
        return list
    return None

map1 = map(find_odd, num_list)
print(map1)
for x in map1:
	print(x)
 
list1 = list(map1)
print(list1)
for x in list1:
	print('list: ',x)
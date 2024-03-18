# def sum_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# result = sum_numbers(1, 2, 3, 4, 5)
# print(result)  # Output: 15

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="John", age=30, city="New York",dog="Dobby")
def my_func(*args, **kwargs):
    print(args)
    print(kwargs)

my_func(1, 2, 3, 6, x=4, y=5)

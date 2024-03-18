import time

start_time_first = time.time()
# outer loop
for i in range(1, 10):
    # inner loop
    for j in range(1, 10):
        print(0, end=" ")
    print()
start_time_first = round(time.time() - start_time_first, 5), "seconds"

start_time_second = time.time()
# outer loop
for i in range(1, 100):
    # inner loop
    for j in range(1, 100):
        print(0, end=" ")
    print()
start_time_second = round(time.time() - start_time_second, 5), "seconds"
# First method to print the tuple using format
print("{} {}".format(start_time_first[0], start_time_first[1]))
print("{} {}".format(start_time_second[0], start_time_second[1]))
# Second method to print the tuple using join
print(' '.join([str(x) for x in start_time_first]))
print(' '.join([str(x) for x in start_time_second]))
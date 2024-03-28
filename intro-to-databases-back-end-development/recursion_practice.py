# def stairs(n):
# 	if n <= 2:
# 		return n
# 	return stairs(n-2)+stairs(n-1)


# count =3
# print(stairs(count))


def stairs(n):
    memo = [0] * (n+1)
    memo[1] = 1
    memo[2] = 2
    print(memo)
    for j in range(3, n+1):
        memo[j] = memo[j-1] + memo[j-2]
    print(memo)
    return memo[j]


count = 3
print(stairs(count))
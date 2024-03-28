def stairs(n):
	if n <= 2:
		return n
	memo = [0]*(n+1)
	memo[1]=1
	memo[2]=2
	for x in range(3,n+1):
		memo[x]= memo[x-1]+memo[x-2]
	return memo[x]

print(stairs(5))
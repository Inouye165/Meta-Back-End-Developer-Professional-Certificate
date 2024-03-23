# def recursive(count):
# 	if count <= 2:
# 		return count
# 	for i in range(count+1):
# 		return recursive(count-1) + recursive(count-2)
# print(recursive(3))
# lamda_method = lambda count: count if count <= 2 else lamda_method(count-1) + lamda_method(count-2)
# print(lamda_method(3))

# def dynamic(count, memo={}):
#   """
#   This function calculates the nth Fibonacci number using dynamic programming (memoization).

#   Args:
#       count: The index of the Fibonacci number to calculate.
#       memo: A dictionary to store previously calculated Fibonacci numbers.

#   Returns:
#       The nth Fibonacci number.
#   """
#   if count in memo:
#     return memo[count]
#   if count <= 2:
#     return count
#   else:
#     result = dynamic(count-1, memo) + dynamic(count-2, memo)
#     memo[count] = result
#     return result
# print(dynamic(3))

# def climb_stairs(count):
#   if count<=2:
#     return count

#   dp = [0] * (count + 1)
#   dp[1] = 1
#   dp[2] = 2

#   for i in range(3, count + 1):
#     dp[i] = dp[i - 1] + dp[i - 2]

#   return dp[count]

# print(climb_stairs(3)) # 3

# def dynamic(count):
#     if count <= 2:
#         return count
#     dp = [0] * (count+1)
#     print(dp)
#     dp[1] = 1
#     dp[2] = 2
#     for i in range(2,count+1):
#         dp[i] = dp[i]+dp[i-1]
#     return dp[count]

# print('first ',dynamic(3))

# def dynamic(count):
# 	if count <= 2:
# 		return count
# 	dp = [0] * (count+1)
# 	dp[1] = 1
# 	dp[2] = 2
# 	for i in range(2,count+1):
# 		dp[i] = dp[i] + dp[i-1]
# 	return dp[count]

dynamic = lambda count: count if count <= 2 else dynamic(count-1) + dynamic(count-2)
print(dynamic(2))
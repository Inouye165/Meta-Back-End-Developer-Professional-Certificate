def recursive(count):
	if count <= 2:
		return count
	if count == 3:
		return 4
	return recursive(count-1) + recursive(count-2) + recursive(count-3)

# print(recursive(3))

def recursive(count):
    return count if count <= 2 else recursive(count - 1) + recursive(count - 2)


print(recursive(3))

def recursive(count):
    return count if count <= 2 else recursive(count - 1) + recursive(count - 2)

fib = lambda n, _fib=lambda self, n: n if n <= 2 else self(self, n-1) + self(self, n-2): _fib(_fib, n)

recursive = (lambda func: lambda n: func(func, n))(lambda self, n: n if n <= 2 else self(self, n-1) + self(self, n-2))
def recursive(count):
	if count <= 2:
		return count
	return recursive(count-1) + recursive(count-2)

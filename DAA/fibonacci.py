def recursive(n):
	if n <= 1:
		return n
	return recursive(n-1) + recursive(n-2)

def non_recursive(n):
    a = 0
    b = 1
    print(a, b, end=' ')
    while (n-2):
        c = a + b
        a , b = b , c
        print(c, end=' ')
        n -= 1

if __name__ == "__main__":
	n = int(input())
	print("Recursive: ")
	for i in range(n):
	    print(recursive(i), end=' ')
	print("\nNon-Recursive")
	non_recursive(n)

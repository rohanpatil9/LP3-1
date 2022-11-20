def recursive(n):
    if n <= 1:
        return n
    return recursive(n-1) + recursive(n-2);

def non_recurive(n):
    a = 0
    b = 1
    print(a, b, end=' ')
    for _ in range(n-2):
        c = a + b
        a , b = b , c
        print(c, end=' ')

if __name__ == '__main__':
    n = int(input())
    print("recursive:")
    for i in range(n):
        print(recursive(i), end=' ')
    print("\nnon_recurive:")
    non_recurive(n)

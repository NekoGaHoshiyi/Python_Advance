

def fib(n):
    if n <= 1:
        return n
    n2 = 0
    n1 = 1
    for i in range(1,n):
        n1 , n2 = n1 + n2, n1
    return n1

print(fib(4))
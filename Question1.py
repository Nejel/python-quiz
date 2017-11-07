1.
a, b = 0, 1
def fibonacci(n):
    for i in range(n):
        a, b = b, a + b

    return a

fib6 = fibonacci(6)

print(fib6)


A. 8
B. 13
C. TypeError
D. UnboundLocalError

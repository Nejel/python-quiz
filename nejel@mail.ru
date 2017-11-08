1.
a, b = 0, 1
def fibonacci(n):
    for i in range(n):
        a, b = b, a + b

    return a

fib6 = fibonacci(6)

print(fib6)

'''
A. 8
B. 13
C. TypeError
D. UnboundLocalError
'''


'''
Traceback (most recent call last):
  File "C:/Users/nezhelsky/Desktop/quiz 1.py", line 8, in <module>
    fib6 = fibonacci(6)
  File "C:/Users/nezhelsky/Desktop/quiz 1.py", line 4, in fibonacci
    a, b = b, a + b
UnboundLocalError: local variable 'b' referenced before assignment
'''

        
        




# Fibonacci Series

a,b=0,1

n=45

for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
    
    
    # By Recursion
    
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(10):
    print(fib(i), end=" ")

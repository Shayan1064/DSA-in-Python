



    #   Parameterized and Functional Rescursion
    
def fact(n, ans=1):
    if n == 0:
        print(ans)   # final answer
        return
    fact(n-1, ans*n)

fact(5)   # Output: 120


# Functional Recursion

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(5))   # Output: 120


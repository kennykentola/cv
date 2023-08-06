from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci(n):
    #check that the input is a positive integer
    if type(n)!=int:
        raise TypeError("n must be a positive integer int")
    if n < 1:
        raise ValueError("n must be a positive integer int")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
for n in range (1, 51):
    print(fibonacci(n+1)/ fibonacci(n))
    


'''fibonacci_cache = {}


def fibonacci(n):
    #if we have cachedthe value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    #compute the nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    #cache the value and return it
    fibonacci_cache[n] = value
    return value
for n in range(1,101):
     print(n, ":", fibonacci(n))'''

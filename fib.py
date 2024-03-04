# Write your code here

def fib(n):
    if n == 0: return 0
    first, second = 0, 1
    for _ in range(n):
        first, second = second, first + second
    return first

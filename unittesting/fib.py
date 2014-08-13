

def fib1(n):
    """nth fibonacci number"""
    a = 0
    b = 1

    if n == 0: return a
    if n == 1: return b

    return fib1(n-1) + fib1(n-2)


def fib2(n):
    """nth fibonnaci number"""
    a = 0
    b = 1

    if n == 0: return a
    if n == 1: return b

    for _ in range(2, n):
        a, b = b, a+b
    return b


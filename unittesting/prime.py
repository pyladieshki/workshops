
import math

def is_prime(n):
    # Brute force testing of primality.  Test against every integer
    # less than a number's square root.
    for i in range(0, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

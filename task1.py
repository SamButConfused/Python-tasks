import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def goldbach(n):
    """Implement Goldbach's conjecture for an even number."""
    if n <= 2 or n % 2 != 0:
        return "Input must be an even integer greater than 2"
    for i in range(2, n // 2 + 1):  # Limit the range to n // 2
        if is_prime(i) and is_prime(n - i):
            return f'{n} can be expressed as {i} + {n - i}'
    return f"No valid pair of primes found for {n}"

# Test cases
print(goldbach(98))  # Output: 6 can be expressed as 3 + 3
print(goldbach(28))  # Output: 28 can be expressed as 5 + 23
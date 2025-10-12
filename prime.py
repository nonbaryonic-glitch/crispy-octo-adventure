#!/usr/bin/env python3
"""
prime.py

Compute and print the 10th prime number.

Deterministic algorithm: iterate integers > 1, test primality by trial
division up to sqrt(n). Stop when we've found the 10th prime and print it.
"""

import math

def is_prime(n: int) -> bool:
    """Return True if n is prime (n >= 2), using trial division."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def nth_prime(n: int) -> int:
    """Return the n-th prime (1-indexed)."""
    if n < 1:
        raise ValueError("n must be >= 1")
    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate

def main():
    """Compute and print the 10th prime number."""
    tenth = nth_prime(10)
    print(tenth)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def sieve_of_eratosthenes(limit: int) -> list[int]:
    """
    Return a list of all prime numbers <= limit.
    """
    # Boolean array where index i represents the number i.
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]          # 0 and 1 are not primes

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            # Mark all multiples of `num` as non‑prime
            step = num
            start = num * num
            is_prime[start:limit+1:step] = [False] * ((limit - start)//step + 1)

    return [i for i, prime in enumerate(is_prime) if prime]


def sum_of_primes(limit: int) -> int:
    primes = sieve_of_eratosthenes(limit)
    return sum(primes)


if __name__ == "__main__":
    LIMIT = 100_000
    total = sum_of_primes(LIMIT)
    print(f"The sum of all prime numbers from 1 to {LIMIT} is: {total}")

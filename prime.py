import timeit
import math


def sieve_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]

    return primes


def disasterCode():
    primes = sieve_eratosthenes(int(math.sqrt(1000)))

    primes_table = {}
    primes_table[1] = set()

    for num in range(2, 1000):
        primes_table[num] = set()
        n = num
        if n not in primes:
            for p in primes:
                if not num % p:
                    primes_table[num].add(p)
                    n //= p
                    primes_table[num] = primes_table[num].union(primes_table[n])
                    break
        else:
            primes_table[num].add(n)


# Benchmark the code
if __name__ == "__main__":
    benchmark_code = "disasterCode()"
    setup_code = "from __main__ import disasterCode"

    # Measure the execution time of disasterCode function
    times = []
    for i in range(0, 5):
        times.append(timeit.timeit(benchmark_code, setup=setup_code, number=1))

    res = sum(times) / 5

    print(f"Average execution time after 5 runs: {res:.6f} seconds")

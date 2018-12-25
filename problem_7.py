import time


def generate_prime():
    """Generator for prime numbers"""
    primes = [2]  # Start with the first prime to compare subsequent
    next_candidate = 3
    it = 0  # For list indexing
    while True:
        for prime in primes:
            if next_candidate % prime == 0:
                # Not a prime
                break
        else:
            # Not divisible by another prime -> is prime
            primes.append(next_candidate)
        next_candidate += 2  # Even numbers past 2 are not prime

        # If there is a new prime number, yield it, otherwise loop until a new prime
        # is found
        if len(primes) > it:
            # Return this prime, pause execution and wait until called again
            yield primes[it]
            # Called again at this point, so increment the iterator and look
            # for more primes
            it += 1


def next_candidate():
    i = 1
    while True:
        yield 6 * i - 1
        yield 6 * i + 1
        i += 1


def generate_prime_2():
    primes = [2, 3]  # Start with the first prime to compare subsequent

    def is_prime(num, primes):
        for prime in primes:
            if num % prime == 0:
                return False
        return True

    it = 0  # For list indexing
    g = next_candidate()
    while True:
        n = next(g)
        if is_prime(n, primes):
            primes.append(n)

        # If there is a new prime number, yield it, otherwise loop until a new prime
        # is found
        if len(primes) > it:
            # Return this prime, pause execution and wait until called again
            yield primes[it]
            # Called again at this point, so increment the iterator and look
            # for more primes
            it += 1


def generate_prime_3():
    """Prime number generator with sieve of Eratosthenes"""
    primes = [True for i in range(105_000)]
    p = 2
    while p ** 2 <= 105_000:
        if primes[p]:
            for i in range(p ** 2, 105_000, p):
                primes[i] = False
        p += 1
    for i in range(105_000):
        if primes[i]:
            yield i


def time_prime(m):
    start = time.perf_counter()
    for i, p in enumerate(m()):
        if i == 10000:  # Zero-based index, but looking for one-based
            result = p
            break
    return result, round(time.perf_counter() - start, 3)


g = [generate_prime, generate_prime_2, generate_prime_3]

for f in g:
    result, duration = time_prime(f)
    print(f"{f.__name__} obtained result: {result} in {duration} sec")

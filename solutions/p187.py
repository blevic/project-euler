MAX_VALUE = 10**8


def first_primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def two_distinct_prime_factors(max_value):
    counter = 0
    primes = first_primes(int(max_value//2) + 1)

    for idx1 in range(len(primes) - 1):
        for idx2 in range(idx1, len(primes)):
            if primes[idx1] * primes[idx2] < max_value:
                counter += 1
            else:
                break
    return counter


if __name__ == '__main__':
    print(two_distinct_prime_factors(MAX_VALUE))

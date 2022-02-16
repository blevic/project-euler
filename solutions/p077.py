def first_primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def prime_summations(n):
    primes = first_primes(n)

    count = [1] + [0]*n
    for p in primes:
        for i in range(n + 1 - p):
            count[i + p] += count[i]
    return count[n]


if __name__ == "__main__":
    number = 0
    while True:
        if prime_summations(number) > 5000:
            break
        number += 1
    print(number)

from itertools import combinations
import sympy

TARGET_FAMILY = 8
ALREADY_CHECKED = set()


def primes_n_digits(n_digits):
    if n_digits == 1:
        return [2, 3, 5, 7]
    n = 10**n_digits
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*int((n-i*i-1)/(2*i)+1)
    return [i for i in range(3, n, 2) if sieve[i] and i > 10**(n_digits-1)]


def try_prime_asterisks(prime, positions):
    prime_s = str(prime)
    base_s = ''
    asterisk_s = ''

    if len(set([prime_s[idx] for idx in positions])) != 1:
        return False

    for idx in range(len(prime_s)):
        if idx in positions:
            base_s += "0"
            asterisk_s += "1"
        else:
            base_s += prime_s[idx]
            asterisk_s += "0"

    base = int(base_s)
    asterisk = int(asterisk_s)

    if (base, asterisk) in ALREADY_CHECKED:
        return False
    else:
        ALREADY_CHECKED.add((base, asterisk))

    count_not_prime = 0
    p0 = 0 in positions

    for i in range(p0, 10):
        test_prime = base + asterisk*i
        if not sympy.isprime(test_prime):
            count_not_prime += 1
        if count_not_prime > (10 - TARGET_FAMILY) - p0:
            return False
    return True


def try_n_digits(n):
    primes = primes_n_digits(n)
    for number_asterisks in range(1, n):
        for asterisks_position in combinations(range(n - 1), number_asterisks):
            for prime in primes:
                if try_prime_asterisks(prime, asterisks_position):
                    return prime


if __name__ == '__main__':
    number_digits = 2
    while True:
        minimal_prime = try_n_digits(number_digits)
        if minimal_prime:
            break
        number_digits += 1
    print(minimal_prime)

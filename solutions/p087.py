MAX_NUMBER = 50000000


def first_primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def prime_powers(power, max_value):
    return [p**power for p in first_primes(int(max_value**(1/power)))]


if __name__ == "__main__":
    prime_squares = prime_powers(2, MAX_NUMBER)
    prime_cubes = prime_powers(3, MAX_NUMBER)
    prime_fourths = prime_powers(4, MAX_NUMBER)

    numbers = set()
    for a in prime_squares:
        for b in prime_cubes:
            for c in prime_fourths:
                if a + b + c < MAX_NUMBER:
                    numbers.add(a + b + c)
    print(len(numbers))

import sympy
import sys

MAX_VALUE = 100000000


def is_prime(n):
    return sympy.isprime(n)


def prime_generating_integer(n):
    for i in range(1, int(n**0.5)+1, n % 2 + 1):
        if n % i == 0:
            if not is_prime(i + n // i):
                return False
    return True


if __name__ == "__main__":
    total = 1 + 2
    for number in range(2, MAX_VALUE + 1, 2):
        if not is_prime(number):
            if prime_generating_integer(number):
                total += number
        if number % (MAX_VALUE/1000) == 0:
            sys.stdout.write('\r')
            percentage = str("%.1f%%" % (100.*number/MAX_VALUE))
            sys.stdout.write(percentage)
            sys.stdout.flush()
    print("\nRESULT: " + str(total))

MOD = 1_000_000_007


def s(n):
    return ((n % 9) + 1)*10**(n//9) - 1


def big_s(k):
    n = k // 9
    r = k % 9 + 2

    return (((r-1)*r + 10) * 10**n - 2*(r + 9*n + 4))//2


def mod_big_s(k):
    n = k//9
    total = (2*(pow(2, n, MOD)*pow(5, n + 2, MOD) - 7) - 9*n) % MOD

    for r in range(k % 9 + 2,  10):
        total -= (r * pow(10, n, MOD) - 1) % MOD

    return total % MOD


def fib_doubling_method(n):
    if n == 0:
        return 0, 1
    else:
        a, b = fib_doubling_method(n // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        if n % 2:
            return d, c + d
        else:
            return c, d


def fib(n):
    return fib_doubling_method(n)[0]


def sum_of_sums():
    return sum(mod_big_s(fib(i)) for i in range(2, 90 + 1)) % MOD


if __name__ == "__main__":
    print(sum_of_sums())

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


def fast_fibonacci(n):
    return fib_doubling_method(n)[0]


def pandigital_bottom(n):
    return set(str(n)[-9:]) == set(str(d) for d in range(1, 10))


def pandigital_top(n):
    return set(str(n)[:9]) == set(str(d) for d in range(1, 10))


def first_pandigital_top_bottom():
    f1, f2, idx = 0, 1, 0
    while True:
        if pandigital_bottom(f1):
            if pandigital_top(fast_fibonacci(idx)):
                return idx
        f1, f2 = f2, (f1 + f2) % 10**9
        idx += 1


if __name__ == "__main__":
    print(first_pandigital_top_bottom())

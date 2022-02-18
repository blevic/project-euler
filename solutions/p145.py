# this is brute forcing, so take a seat

def odd_digits(n):
    r = 0
    while n > 0:
        r *= 10
        if n % 2 == 0:
            return False
        n //= 10
    return True


def reverse_n(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n //= 10
    return r


def is_reversible(n):
    if n % 10 == 0:
        return False
    return odd_digits(n + reverse_n(n))


if __name__ == "__main__":
    print(sum(is_reversible(i) for i in range(1, 10**9)))

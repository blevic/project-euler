from math import gcd

MIN_SOLUTIONS = 10**6


def pythagorean_legs(max_value):
    for m in range(int((max_value - 1) ** 0.5) + 1):
        for n in range(1 + m % 2, min(m, int((max_value - m * m) ** 0.5) + 1), 2):
            if gcd(m, n) > 1:
                continue
            c1 = m*m - n*n
            c2 = 2*m*n
            h = m*m + n*n
            for k in range(1, max_value//h + 1):
                yield k*c1, k*c2
                yield k*c2, k*c1


def solutions(n):
    return sum(count_divisions(legs) for legs in pythagorean_legs(int(n*5**0.5)) if legs[0] <= n)


def count_divisions(p):
    return max(min(p[0], p[1] - 1) - (p[1] - 1)//2, 0)


def unbounded_binary_search(min_solutions):
    m, low, high = 1, 1, 1
    while True:
        sol = solutions(m)
        if sol >= min_solutions:
            high = m
            m = low + (high - low)//2
        else:
            low = m
            m *= 2
        if high - low == 1:
            return high


if __name__ == "__main__":
    print(unbounded_binary_search(MIN_SOLUTIONS))

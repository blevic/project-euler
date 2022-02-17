from math import gcd
from collections import defaultdict


def pythagorean_triples(max_value):
    limit_c = max_value // 2
    for m in range(int((limit_c - 1) ** 0.5) + 1):
        for n in range(1 + m % 2, min(m, int((limit_c - m * m) ** 0.5) + 1), 2):
            if gcd(m, n) > 1:
                continue
            c1 = m*m - n*n
            c2 = 2*m*n
            h = m*m + n*n
            for k in range(1, limit_c // h + 1):
                if k*c1 + k*c2 + k*h <= max_value:
                    yield k*c1, k*c2, k*h


if __name__ == '__main__':
    MAX_VALUE = 1500000
    all_lengths = defaultdict(int)
    for triple in pythagorean_triples(MAX_VALUE):
        all_lengths[sum(triple)] += 1

    print(sum(all_lengths[x] == 1 for x in all_lengths))

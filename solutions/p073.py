from math import gcd


def coprimes(a, b):
    return gcd(a, b) == 1


counter = 0
for d in range(1, 12001):
    for n in range(int(d/3), int(d/2) + 1):
        if coprimes(d, n) and 1/2 > n/d > 1/3:
            counter += 1

print(counter)

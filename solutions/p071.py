from math import gcd


def coprimes(a, b):
    return gcd(a, b) == 1


target = 3/7
best_num = 0
best_den = 1
for den in range(1, 1000001):
    num = int(target*den)
    while num/den > best_num/best_den and den != 7:
        if coprimes(num, den):
            best_num = num
            best_den = den
        num -= 1

print(best_num)

# VERY SLOW, this will take some minutes -- but it works!
import time
import math

t0 = time.time()


def length(n):
    if n > 0:
        return int(math.log10(n)) + 1
    else:
        return 1


def split_it(s):
    yield s
    n_digits = length(s)
    if n_digits > 1:
        for i in range(1, n_digits):
            for l1 in split_it(s % 10**i):
                yield l1 + s // 10**i


def compute_solution():
    total = 0
    for root in range(9, 10**6 + 1):
        if root % 9 == 1 or root % 9 == 0:
            for split_sum in split_it(root**2):
                if split_sum == root:
                    t = time.time() - t0
                    print(str(t)[:7] + "s -> " + "{:.2%}".format(root/10**6) + " -> " + str(root**2))
                    total += root**2
                    break
    print("TOTAL: " + str(total))


if __name__ == '__main__':
    compute_solution()
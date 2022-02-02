# EXTREMELY SLOW, this will take a long time -- but it works!
import time

t0 = time.time()


def split_it(s):
    yield int(s)
    if len(s) > 1:
        for i in range(1, len(s)):
            for l1 in split_it(s[:i]):
                yield l1 + int(s[i:])


def slow_solution():
    total = 0
    for root in range(9, 10**6 + 1):
        if root % 9 == 1 or root % 9 == 0:
            for split_sum in split_it(str(root**2)):
                if split_sum == root:
                    t = time.time() - t0
                    print(str(t)[:7] + "s -> " + "{:.2%}".format(root/10**6) + " -> " + str(root**2))
                    total += root**2
                    break
    print("TOTAL: " + str(total))


if __name__ == '__main__':
    slow_solution()
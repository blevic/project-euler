# EXTREMELY SLOW, this will take a long time -- but it works!
import time

t0 = time.time()


def split_it(s):
    yield int(s)
    if len(s) > 1:
        for i in range(1, len(s)):
            for l1 in split_it(s[:i]):
                yield l1 + int(s[i:])


total = 0
for root in range(4, 10**6 + 1):
    for split_sum in split_it(str(root**2)):
        if split_sum == root:
            t = time.time() - t0
            print(str(t)[:7] + "s -> " + "{:.2%}".format(root/10**6) + " -> " + str(root**2))
            total += root**2
            break


print("TOTAL: " + str(total))  # 1-2-8-0-8-8-8-3-0-5-4-7-9-8-2

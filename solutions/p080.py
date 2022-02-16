from decimal import *


def first_hundred_digits_sum_sqrt(n):
    if (n**0.5).is_integer():
        return 0
    getcontext().prec = 102
    hundred_digits = str(Decimal(n).sqrt()).replace(".", "")[:100]
    return sum([int(d) for d in hundred_digits])


if __name__ == "__main__":
    print(sum(first_hundred_digits_sum_sqrt(i) for i in range(101)))

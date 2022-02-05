from math import factorial


def chain_sixty(n):
    chain = [n]
    number = n
    while True:
        str_n = str(number)
        next_number = 0
        for d in str_n:
            next_number += factorial(int(d))
        number = next_number
        if number in chain:
            return len(chain) == 60
        else:
            chain.append(number)


print(sum([chain_sixty(i) for i in range(1, 1000001)]))

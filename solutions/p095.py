from functools import reduce


class AmicableChain:
    def __init__(self, starting_point):
        self.starting_point = starting_point
        self.is_amicable = False
        self.chain = [starting_point]
        self.length = 1
        self.build()

    def build(self):
        i = self.starting_point
        while True:
            next_i = sum_proper_factors(i)
            if next_i == self.starting_point:
                self.is_amicable = True
                return
            elif next_i in self.chain or next_i > 10 ** 6:
                return
            else:
                self.chain.append(next_i)
                self.length += 1
                i = next_i


def all_factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def sum_proper_factors(n):
    if n:
        return sum(all_factors(n)) - n
    else:
        return 0


def smallest_in_longest_chain():
    max_chain = AmicableChain(0)
    for number in range(10**6 + 1):
        chain = AmicableChain(number)
        if chain.is_amicable and chain.length > max_chain.length:
            max_chain = chain

    return min(max_chain.chain)


if __name__ == "__main__":
    print(smallest_in_longest_chain())

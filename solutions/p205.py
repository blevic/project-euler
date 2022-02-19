from itertools import product
from collections import defaultdict


def probability():
    peter = defaultdict(int)
    collin = defaultdict(int)
    cumulative_c = dict()

    for p_round in product(range(1, 5), repeat=9):
        peter[sum(p_round)] += 1

    for c_round in product(range(1, 7), repeat=6):
        collin[sum(c_round)] += 1

    for key in collin:
        cumulative_c[key] = cumulative_c[key - 1] + collin[key - 1] if key - 1 in cumulative_c else 0

    peter_wins = sum(peter[k]*cumulative_c[k] for k in peter)
    total_rounds = sum(peter.values()) * sum(collin.values())

    return peter_wins/total_rounds



if __name__ == "__main__":
    print('{0:.7f}'.format(probability()))

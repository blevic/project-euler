from itertools import permutations

max_string = ""

for p in permutations(reversed(range(1, 10))):
    e = list(p[:4]) + [10]  # 10 should be external due to 16-digit restriction
    e = e[e.index(min(e)):] + e[:e.index(min(e))]  # rotate external ring to start at minimum value
    for r in itertools.permutations(p[4:]):
        for i in range(5):
            if e[i] + r[i] != e[(i + 1) % 5] + r[(i + 2) % 5]:
                break
        else:
            candidate_string = "".join([str(100*e[i] + 10*r[i] + r[(i + 1)%5]) for i in range(5)])
            if candidate_string > max_string:
                max_string = candidate_string
print(max_string)

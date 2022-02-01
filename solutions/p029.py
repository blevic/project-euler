# How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

distinct_terms = set()

for a in range(2, 100+1):
    for b in range(2, 100+1):
        if a**b not in distinct_terms:
            distinct_terms.add(a**b)

print(len(distinct_terms))

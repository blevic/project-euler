sequence = [2, 1, 2]
counter = 3
while counter < 100:
    if counter % 3 == 2:
        sequence.append(sequence[-3] + 2)
    else:
        sequence.append(1)
    counter += 1

frac = (1, sequence[-1])
for n in reversed(sequence[:-1]):
    frac = (frac[1], n*frac[1] + frac[0])

print(sum(int(x) for x in str(frac[1])))

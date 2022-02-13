def A000041(n):  # integer partitions is a sequence in the OEIS
    sequence = [1] + [0]*n
    for i in range(1, n + 1):
        for j in range(i, len(sequence)):
            sequence[j] += sequence[j - i]
    return sequence[n]


if __name__ == "__main__":
    print(A000041(100) - 1)  # removes trivial case (1 term)

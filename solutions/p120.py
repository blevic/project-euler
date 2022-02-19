def max_remainder(a):
    return a*(a - 1) if a % 2 else a*(a - 2)


if __name__ == "__main__":
    print(sum(max_remainder(a) for a in range(3, 1001)))

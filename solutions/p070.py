from sympy import totient


def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


if __name__ == "__main__":
    minimum_n = 1
    minimum_ratio = 10
    for n in range(2, 10**7):  # VERY SLOW, go take a coffee
        phi_n = totient(n)
        if n/phi_n < minimum_ratio and is_permutation(n, phi_n):
            minimum_n = n
            minimum_ratio = n/phi_n

    print(minimum_n)

MAX_VALUE = 10**3


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def sum_squares(a, b):
    return (1 + b - a)*(2*a*a + 2*a*b - a + 2*b*b + b)//6


def palindromic_sums(limit):
    palindromes = set()
    a1 = 1
    while a1**2 < limit:
        a2 = a1 + 1
        while True:
            candidate = sum_squares(a1, a2)
            if candidate > limit:
                break
            if is_palindrome(candidate):
                palindromes.add(candidate)
            a2 += 1
        a1 += 1
    return palindromes


if __name__ == "__main__":
    print(sum(palindromic_sums(MAX_VALUE)))

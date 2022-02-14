from sympy import totient

print(sum(totient(d) for d in range(2, 1000001)))  # sorry not sorry

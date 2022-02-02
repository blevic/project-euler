import sympy

max_frac, max_frac_n = 0, 0
for n in range(2, 1000001):
    frac = n/sympy.totient(n)  # oh to be lazy
    if frac > max_frac:
        max_frac = frac
        max_frac_n = n
print(max_frac_n)

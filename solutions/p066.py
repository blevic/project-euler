def is_square(n):
    return (n**0.5).is_integer()


def pell_fundamental_solution(n):
    if n < 0 or is_square(n):
        return -1, -1

    x = int(n**0.5)
    y, z, r = x, 1, x << 1
    e1, e2 = 1, 0
    f1, f2 = 0, 1
    while True:
        y = r*z - y
        z = (n - y*y)//z
        r = (x + y)//z

        e1, e2 = e2, e1 + e2*r
        f1, f2 = f2, f1 + f2*r

        a, b = f2 * x + e2, f2
        if a*a - n*b*b - 1 == 0:
            return a, b


if __name__ == "__main__":
    max_x, max_d = 0, 0
    for d in range(1000):
        x, y = pell_fundamental_solution(d)
        if max_x < x:
            max_x, max_d = x, d

    print(max_d)

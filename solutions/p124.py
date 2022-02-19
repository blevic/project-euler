def rad(n):
    product = 1
    while n > 1:
        for i in range(2, int(n + 1)):
            if n % i == 0:
                n /= i
                if product % i:
                    product *= i
                break
    return product


if __name__ == "__main__":
    e = []
    for i in range(1, 100001):
        e.append([i, rad(i)])
    e.sort(key=lambda x: x[1])
    print(e[9999][0])

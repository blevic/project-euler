MEGA = 10**6
MAX_VALUE = 1000


def find_mega_partition(max_value):
    pentagons = [0]*max_value
    for i in range(max_value):
        pentagons[i] = int(pentagon(i))

    n = 1
    partitions = [1] + [0]*max_value

    while partitions[n - 1] % MEGA:
        i, sign = 0, -1
        while True:
            x = n - pentagons[i + 1]
            if x < 0:
                break
            if i % 2 == 0:
                sign *= -1
            try:
                partitions[n] += sign * partitions[x]
            except IndexError:
                return False
            i += 1
        n += 1
    return n - 1


def pentagon(n):
    i = (n + 1) / 2 if n%2 else - n/2
    return (i*(3*i - 1))/2


if __name__ == "__main__":
    while True:
        result = find_mega_partition(MAX_VALUE)
        if result:
            break
        else:
            MAX_VALUE *= 10
    print(result)
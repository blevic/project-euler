def is_increasing(n):
    c0 = str(n)[0]
    for c in str(n):
        if c0 > c:
            return False
        c0 = c
    return True

def is_decreasing(n):
    c0 = str(n)[0]
    for c in str(n):
        if c0 < c:
            return False
        c0 = c
    return True

def is_bouncy(n):
    if not is_increasing(n) and not is_decreasing(n):
        return True
    else:
        return False

if __name__ == "__main__":
    count = 0
    i = 100
    while True:
        if is_bouncy(i):
            count += 1
        if count*100 >= 99*i:
            break
        i += 1
    print(i)
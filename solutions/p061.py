def cycle_lst(category):
    lst = []
    n, number = 1, 1
    while number < 10000:
        if number > 999:
            lst.append(number)
        n += 1
        if category == 3:
            number = n*(n + 1)//2
        elif category == 4:
            number = n * n
        elif category == 5:
            number = n*(3*n - 1)//2
        elif category == 6:
            number = n*(2*n - 1)
        elif category == 7:
            number = n*(5*n - 3)//2
        elif category == 8:
            number = n*(3*n - 2)
        else:
            break
    return lst


def can_it_be_in_the_cycle(number, idx, P_lsts):
    lhs = []
    rhs = []
    for i in range(9):
        if idx == i:
            continue
        for n in P_lsts[i]:
            if str(number)[0:2] == str(n)[2:4] and i not in lhs:
                lhs.append(i)
            if str(number)[2:4] == str(n)[0:2] and i not in rhs:
                rhs.append(i)

    if len(lhs) == 0 or len(rhs) == 0:
        return False
    if len(lhs) == 1 and len(rhs) == 1 and lhs == rhs:
        return False

    return True



if __name__ == '__main__':
    P_lists = [[] for _ in range(9)]
    for i in range(3, 9):
        P_lists[i] = cycle_lst(i)

    total = 0
    for i in range(3, 9):
        total += len(P_lists[i])

    print(total)

    P_shrunk = [[] for _ in range(9)]
    for i in range(3, 9):
        for n in P_lists[i]:
            if can_it_be_in_the_cycle(n, i, P_lists):
                P_shrunk[i].append(n)

    total = 0
    for i in range(3, 9):
        total += len(P_shrunk[i])

    print(total)

    for i in range(3, 9):
        print(P_shrunk[i])
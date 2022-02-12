class Nonagon:
    def __init__(self, number, category):
        self.number = number
        self.category = category
        self.first_half = str(number)[0:2]
        self.second_half = str(number)[2:4]
        self.can_come_from = []
        self.can_go_to = []

    def add_can_go_to(self, obj):
        self.can_go_to.append(obj)

    def add_can_come_from(self, obj):
        self.can_come_from.append(obj)


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


def create_object(number, idx, P_lsts):
    ngon_object = Nonagon(number, idx)
    for category in range(9):
        if category == idx:
            continue
        for n in P_lsts[category]:
            if ngon_object.first_half == str(n)[2:4]:
                ngon_object.add_can_come_from(Nonagon(n, category))
            if ngon_object.second_half == str(n)[0:2]:
                ngon_object.add_can_go_to(Nonagon(n, category))
    return ngon_object


def initial_list():
    P_lists = [[] for _ in range(9)]
    for i in range(3, 9):
        P_lists[i] = cycle_lst(i)

    return P_lists


def search(objects, categories, P_objects):
    if sorted(categories) == list(range(3, 9)) and objects[0].first_half == objects[-1].second_half:
        print(sum(obj.number for obj in objects))
        return True

    for e in objects[-1].can_go_to:
        target_cat = e.category
        target_num = e.number
        if target_cat not in categories:
            for obj in P_objects[target_cat]:
                if obj.number == target_num:
                    break
            search(objects + [obj], categories + [target_cat], P_objects)


if __name__ == '__main__':
    # create list with all n-gon numbers
    P_lists = initial_list()
    len_list = sum(len(P_lists[i]) for i in range(9))

    # create reduced list with all numbers that have a possible origin and a possible destination
    P_shrunk = [[] for _ in range(9)]
    for i in range(3, 9):
        for n in P_lists[i]:
            if can_it_be_in_the_cycle(n, i, P_lists):
                P_shrunk[i].append(n)

    len_shrunk = sum(len(P_shrunk[i]) for i in range(9))

    # shrink the list repeatedly
    while len_list > len_shrunk:
        P_lists = P_shrunk
        len_list = sum(len(P_lists[i]) for i in range(9))
        P_shrunk = [[] for _ in range(9)]
        for i in range(3, 9):
            for n in P_lists[i]:
                if can_it_be_in_the_cycle(n, i, P_lists):
                    P_shrunk[i].append(n)
        len_shrunk = sum(len(P_shrunk[i]) for i in range(9))

    # classify all numbers in to/from categories
    P_objects = [[] for _ in range(9)]
    for category in range(3, 9):
        for number in P_shrunk[category]:
            P_objects[category].append(create_object(number, category, P_shrunk))

    # compute result with recursive function
    for e in P_objects[3]:
        search([e], [3], P_objects)

MIN_VALUE = 10**12


def solution(min_value):
    x = 1  # x = 2*blue_discs - 1    =>  2*blue_discs*(blue_discs - 1) == total_discs*(total_discs - 1)
    y = 1  # y = 2*total_discs - 1   =>  x**2 - 2*y**2 = -1

    while True:
        x, y = 3*x + 4*y, 2*x + 3*y
        total_discs, blue_discs = (x + 1)//2, (y + 1)//2

        if total_discs > min_value:
            return blue_discs


if __name__ == "__main__":
    print(solution(MIN_VALUE))

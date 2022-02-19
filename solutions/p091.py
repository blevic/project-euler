from itertools import product


class Triangle:
    def __init__(self, p0, p1, p2):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.d01 = None
        self.d12 = None
        self.d02 = None
        self.define_distances()

    def is_right(self):
        if self.d01 == 0 or self.d12 == 0 or self.d02 == 0:
            return False
        else:
            return self.d01 == self.d12 + self.d02 or self.d12 == self.d01 + self.d02 or self.d02 == self.d12 + self.d01

    def define_distances(self):
        def square_of_distance(point_1, point_2):
            return (point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2

        self.d01 = square_of_distance(self.p0, self.p1)
        self.d12 = square_of_distance(self.p1, self.p2)
        self.d02 = square_of_distance(self.p0, self.p2)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def number_of_right_triangles():
    return sum(Triangle(Point(0, 0), Point(p[0], p[1]), Point(p[2], p[3])).is_right()
               for p in product(range(0, 51), repeat=4)) // 2


if __name__ == "__main__":
    print(number_of_right_triangles())

class ContinuedFractionSqrt:
    def __init__(self, number):
        self.number = number
        self.integer_part = None
        self.continued_fraction = None
        self.calculate_integer_part(number)
        self.calculate_continued_fraction(number)

    def calculate_integer_part(self, number):
        self.integer_part = int(number**0.5)

    def calculate_continued_fraction(self, number):
        self.continued_fraction = []
        if self.integer_part**2 == number:
            return

        a, p, q = self.integer_part, 0, 1
        while True:
            p = a*q - p
            q = (number - p*p)//q
            a = (self.integer_part + p)//q
            self.continued_fraction.append(a)
            if q == 1:
                break
        return


def odd_period_sqrt(number):
    return len(ContinuedFractionSqrt(number).continued_fraction) % 2


if __name__ == "__main__":
    print(sum(odd_period_sqrt(n) for n in range(1, 10001)))

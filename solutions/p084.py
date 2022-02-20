from random import randint
from collections import defaultdict

NUMBER_OF_ROUNDS = 10**6
DICE_SIZE = 4

GO = 0
A1 = 1
CC1 = 2
A2 = 3
T1 = 4
R1 = 5
B1 = 6
CH1 = 7
B2 = 8
B3 = 9
JAIL = 10
C1 = 11
U1 = 12
C2 = 13
C3 = 14
R2 = 15
D1 = 16
CC2 = 17
D2 = 18
D3 = 19
FP = 20
E1 = 21
CH2 = 22
E2 = 23
E3 = 24
R3 = 25
F1 = 26
F2 = 27
U2 = 28
F3 = 29
G2J = 30
G1 = 31
G2 = 32
CC3 = 33
G3 = 34
R4 = 35
CH3 = 36
H1 = 37
T2 = 38
H2 = 39


class Monopoly:
    def __init__(self):
        self.pos = 0
        self.dice_size = DICE_SIZE
        self.double = 0
        self.cc_counter = 0
        self.chance_counter = 0
        self.final_squares = defaultdict(int)

    def play_n_rounds(self, n):
        self.double = 0
        for _ in range(n):
            self.play_once()

    def play_once(self):
        d1, d2 = randint(1, self.dice_size), randint(1, self.dice_size)
        if d1 == d2:
            self.double += 1
            if self.double == 3:
                self.go_to(JAIL)
                self.double = 0
                return
        else:
            self.double = 0

        self.pos = (self.pos + d1 + d2) % 40

        if self.pos in (CC1, CC2, CC3):
            self.got_cc()
        elif self.pos in (CH1, CH2, CH3):
            self.got_chance()
        elif self.pos == G2J:
            self.go_to(JAIL)
        else:
            self.go_to(self.pos)

    def go_to(self, destination):
        self.pos = destination
        self.final_squares[destination] += 1

    def got_cc(self):
        self.cc_counter = (self.cc_counter + 1) % 16
        if self.cc_counter == 1:
            self.go_to(GO)
        elif self.cc_counter == 2:
            self.go_to(JAIL)
        else:
            self.go_to(self.pos)

    def got_chance(self):
        self.chance_counter = (self.chance_counter + 1) % 16
        if self.chance_counter == 1:
            self.go_to(GO)
        elif self.chance_counter == 2:
            self.go_to(JAIL)
        elif self.chance_counter == 3:
            self.go_to(C1)
        elif self.chance_counter == 4:
            self.go_to(E3)
        elif self.chance_counter == 5:
            self.go_to(H2)
        elif self.chance_counter == 6:
            self.go_to(R1)
        elif self.chance_counter in (7, 8):
            if self.pos == CH1:
                self.go_to(R2)
            elif self.pos == CH2:
                self.go_to(R3)
            else:
                self.go_to(R1)
        elif self.chance_counter == 9:
            if self.pos == CH2:
                self.go_to(U2)
            else:
                self.go_to(U1)
        elif self.chance_counter == 10:
            self.go_to(self.pos - 3)
        else:
            self.go_to(self.pos)

    def most_popular_squares(self):
        sorted_squares = sorted(self.final_squares.items(), key=lambda item: -item[1])
        return f"{sorted_squares[0][0]:02d}" + f"{sorted_squares[1][0]:02d}" + f"{sorted_squares[2][0]:02d}"


if __name__ == "__main__":
    game = Monopoly()
    game.play_n_rounds(NUMBER_OF_ROUNDS)
    print(game.most_popular_squares())  # probable result (Monte Carlo method)

MIN_ROOT = int(1020304050607080900 ** 0.5)
MAX_ROOT = int(1929394959697989900 ** 0.5)

base1 = (MIN_ROOT // 100) * 100 + 30    # the root needs to end with -0 to have -0 as its square final digit
base2 = (MIN_ROOT // 100) * 100 + 70    # the square needs to end with -00 as it has -0 as root
                                        # the root needs to end with -30 or -70 to have -900 as square final digit


def good_format(n):
    s = str(n)
    return s[0] + s[2] + s[4] + s[6] + s[8] + s[10] + s[12] + s[14] + s[16] + s[18] == "1234567890"


n1 = base1
n2 = base2

while True:
    if good_format(n1 * n1):
        print(n1)
        break
    if good_format(n2 * n2):
        print(n2)
        break

    if n1 > MAX_ROOT:
        print("ERROR")
        break

    n1 += 100
    n2 += 100

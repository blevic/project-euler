DICTIO = {}

n = 1
while True:
    key = "".join(sorted(str(n**3)))
    if key in DICTIO:
        DICTIO[key].append(n)
        if len(DICTIO[key]) == 5:
            break
    else:
        DICTIO[key] = [n]
    n += 1

print(DICTIO[key][0]**3)

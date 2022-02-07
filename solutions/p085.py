def number_of_rectangles(width, height):
    total = 0
    total += width*height  # 1x1 squares
    total += width*(width - 1)*height//2  # horizontal rectangles
    total += height*(height - 1)*width//2  # vertical rectangles
    total += height*width*(height - 1)*(width - 1)//4  # other rectangles (fat rectangles)
    return total


best_case = 0
best_area = 0
for a in range(1000):
    for b in range(1000):
        if abs(best_case - 2000000) > abs(number_of_rectangles(a, b) - 2000000):
            best_case = number_of_rectangles(a, b)
            best_area = a*b

print(best_area)

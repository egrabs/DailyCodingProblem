# Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C,
# replace the color of the given pixel and all adjacent same colored pixels with C.

# For example, given the following matrix, and location pixel of (1, 1), and 'G' for green:

# B B W
# W W W
# W W W
# B B B

# Becomes

# B B G
# G G G
# G G G
# B B B

def replacePixels(img, loc, color):
    y, x = loc
    orig = img[x][y]
    for dx in (-1, 0, 1):
        x_new = x+dx
        if x_new < 0 or x_new >= len(img[0]):
            continue
        for dy in (-1, 0, 1):
            y_new = y+dy
            if y_new < 0 or y_new >= len(img):
                continue
            if img[y_new][x_new] == orig:
                img[y_new][x_new] = color
    return img


tst = [['B', 'B', 'W'],
 ['W', 'W', 'W'],
 ['W', 'W', 'W'],
 ['B', 'B', 'B']
]

print(replacePixels(tst, (1,1), 'G'))
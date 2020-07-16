"""
Prog:   ex-03.py

Auth:   R. Morgan

Desc:   Demonstrate how to use John Zelle's
        aphics.py library to draw lines
        at random positions and colors
        in the window using points.

Lic:    This code is placed in the public domain.

"""

from graphics import *
from random import randint


# Bresenham's line drawing algorithm
# to handle lines of any orientation
def line(x1, y1, x2, y2, color, win):
    # Calculate dx, sx
    dx = x2 - x1
    if dx < 0:
        sx = -1
    else:
        sx = 1
    # calculate dy, sy
    dy = y2 - y1
    if dy < 0:
        sy = -1
    else:
        sy = 1

    if abs(dx) > abs(dy):
        slope = dy / dx
        pitch = y1 - slope * x1
        while x1 != x2:
            y = slope * x1 + pitch
            p = Point(x1, y)
            p.setFill(color)
            p.draw(win)
            x1 += sx
    else:
        slope = dx / dy
        pitch = x1 - slope * y1
        while y1 != y2:
            x = slope * y1 + pitch
            p = Point(x, y1)
            p.setFill(color)
            p.draw(win)
            y1 += sy


def vertLine(x, y1, y2, color, win):
    for y in range(y1, y2):
        p = Point(x, y)
        p.setFill(color)
        p.draw(win)


def horzLine(x1, y1, x2, color, win):
    for x in range(x1, x2):
        p = Point(x, y1)
        p.setFill(color)
        p.draw(win)


def main():
    width = 640
    height = 480
    colour = None
    max_x = width-10
    min_x = 10
    max_y = height-10
    min_y = 10
    num_steps = 20
    delta_x = (max_x - min_x) / num_steps
    delta_y = (max_y - min_y) / num_steps

    win = GraphWin("Lines 2", width, height)
    win.setBackground(color_rgb(0, 0, 0))

    # Draw 10,000 points in the window
    # each with a random colour and at a
    # random position/
    x = min_x
    y = min_y
    while x < max_x:
        # Set random colour
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        # Draw our line using generated coordinates and colour
        line(x, min_y, max_x, y, color_rgb(r, g, b), win)

        x += delta_x
        y += delta_y

    colour = color_rgb(255, 255, 228)

    # line(width / 2, 0, 0, height / 2, colour, win)
    # line(0, height / 2, width / 2, height, colour, win)
    # line(width / 2, height, width, height / 2, colour, win)
    # line(width, height / 2, width / 2, 0, colour, win)
    line(min_x, min_y, max_x, min_y, colour, win)
    line(max_x, min_y, max_x, max_y, colour, win)
    line(max_x, max_y, min_x, max_y, colour, win)
    line(min_x, max_y, min_x, min_y, colour, win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()

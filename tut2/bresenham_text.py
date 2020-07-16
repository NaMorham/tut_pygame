#! /usr/bin/env python

import logging
import math


g_logger = logging.getLogger()
degree_sign = u'\N{DEGREE SIGN}'


def vert_line(x, y1, y2, end_cap=True):  #, color, win):
    logging.debug("calc vert line from ({}, {}) to ({}, {})".format(x, y1, x, y2))
    if y2 < y1:
        delta = -1
    else:
        delta = 1
    point_data = []
    for y in range(y1, y2, delta):
        # p = Point(x, y)
        # p.setFill(color)
        # p.draw(win)
        point_data.append([x, y])
        logging.debug("point ({}, {})".format(x, y))
    if end_cap:
        point_data.append([x, y2])
        logging.debug("point ({}, {})".format(x, y2))
    return point_data


def horiz_line(x1, y1, x2, end_cap=True):  #, color, win):
    logging.debug("calc horiz line from ({}, {}) to ({}, {})".format(x1, y1, x2, y1))
    if x2 < x1:
        delta = -1
    else:
        delta = 1
    point_data = []
    for x in range(x1, x2, delta):
        # p = Point(x, y1)
        # p.setFill(color)
        # p.draw(win)
        point_data.append([x, y1])
        logging.debug("point ({}, {})".format(x, y1))
    if end_cap:
        point_data.append([x2, y1])
        logging.debug("point ({}, {})".format(x2, y1))
    return point_data


# Bresenham's line drawing algorithm
# to handle lines of any orientation
def line(x1, y1, x2, y2, end_cap=True):  #, color, win):
    point_data = []
    logging.debug("calc line from ({}, {}) to ({}, {})".format(x1, y1, x2, y2))
    # Calculate dx, sx
    dx = x2 - x1
    if dx < 0:
        sx = -1
    else:
        sx = 1
    logging.debug("dx = {}, sx = {}".format(dx, sx))
    # calculate dy, sy
    dy = y2 - y1
    if dy < 0:
        sy = -1
    else:
        sy = 1
    logging.debug("dy = {}, sy = {}".format(dy, sy))

    if abs(dx) > abs(dy):
        slope = dy / dx
        pitch = y1 - slope * x1
        logging.debug("abs({}) > abs({}), slope = {}, pitch = {}".format(dx, dy, slope, pitch))
        while x1 != x2:
            y = int(slope * x1 + pitch)
            # p = Point(x1, y)
            # p.setFill(color)
            # p.draw(win)
            point_data.append([x1, y])
            logging.debug("point ({}, {})".format(x1, y))
            x1 += sx
    else:
        slope = dx / dy
        pitch = x1 - slope * y1
        logging.debug("abs({}) <= abs({}), slope = {}, pitch = {}".format(dx, dy, slope, pitch))
        while y1 != y2:
            x = int(slope * y1 + pitch)
            # p = Point(x, y1)
            # p.setFill(color)
            # p.draw(win)
            point_data.append([x, y1])
            logging.debug("point ({}, {})".format(x, y1))
            y1 += sy
    if end_cap:
        point_data.append([x2, y2])
        logging.debug("point ({}, {})".format(x2, y2))
    return point_data


if __name__ == "__main__":
    # g_logger.setLevel(logging.DEBUG)
    g_logger.setLevel(logging.INFO)
    logging.debug("Start...")

    print("Horiz. lines")
    tmp_points = horiz_line(10, 10, 20)
    print(tmp_points)
    tmp_points = horiz_line(10, 10, 10)
    print(tmp_points)
    tmp_points = horiz_line(-5, 10, 5)
    print(tmp_points)
    print("{}\n".format("-"*60))

    print("Vert. lines")
    tmp_points = vert_line(10, 10, 20)
    print(tmp_points)
    tmp_points = vert_line(10, 10, 10)
    print(tmp_points)
    tmp_points = vert_line(10, 20, 10)
    print(tmp_points)
    tmp_points = vert_line(10, -5, 5)
    print(tmp_points)
    print("{}\n".format("-"*60))

    print("lines")
    tmp_points = line(10, 10, 20, 20)
    print(tmp_points)
    tmp_points = line(20, 20, 10, 10)
    print(tmp_points)
    tmp_points = line(10, 10, 20, 15)
    print(tmp_points)
    tmp_points = line(-5, -5, 5, 5)
    print(tmp_points)
    tmp_points = line(5, 5, -5, -5)
    print(tmp_points)
    print("{}".format("-"*60))
    tmp_points = line(0, 0, 5, 5)
    print(tmp_points)
    tmp_points = line(0, 0, 5, -5)
    print(tmp_points)
    tmp_points = line(0, 0, -5, -5)
    print(tmp_points)
    tmp_points = line(0, 0, -5, 5)
    print(tmp_points)
    print("{}\n".format("-"*60))

    for d in range(0, 360, 10):
        x_val = int(math.cos(math.radians(d))*10)
        y_val = int(math.sin(math.radians(d))*10)
        logging.debug("{}{} --> ({}, {})".format(d, degree_sign, x_val, y_val))
        tmp_points = line(0, 0, x_val, y_val)
        print("{}{} -> {}".format(d, degree_sign, tmp_points))

    r1 = 15
    r2 = 20
    for d in range(0, 360, 10):
        x_val = int(math.cos(math.radians(d))*r1)
        y_val = int(math.sin(math.radians(d))*r1)
        x_val2 = int(math.cos(math.radians(d))*r2)
        y_val2 = int(math.sin(math.radians(d))*r2)
        logging.debug("{}{} --> ({}, {}) -> ({}, {})".format(d, degree_sign, x_val, y_val, x_val2, y_val2))
        tmp_points = line(x_val, y_val, x_val2, y_val2)
        print("{}{} -> {}".format(d, degree_sign, tmp_points))

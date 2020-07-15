#! /usr/bin/env python

import random


def simple_test1(num_values=100, num_per_row=10, max_val=10, min_val=1):
    num_values = int(num_values)
    num_per_row = int(num_per_row)
    min_val = int(min_val)
    max_val = int(max_val)

    num_values = num_values if num_values >= 1 else 1
    num_per_row = num_per_row if num_per_row >= 1 else 1
    if min_val > max_val:
        tmp_val = max_val
        max_val = min_val
        min_val = tmp_val

    for i in range(num_values):
        if (i % num_per_row) == 0:
            print("{:5d}: ".format(i), end="")

        print("{:3d}, ".format(random.randrange(min_val, max_val+1)), end="")

        if ((i+1) % num_per_row) == 0:
            print()
    # if the last thing was not a new line, add one
    if (num_values % num_per_row) != 0:
        print()

    for i in range(num_values):
        print("{}".format("+" if random.randrange(10)+1 > 5 else "-"), end="")
    print("\n")


def print_histo(histo, min_val):
    max_indices = [i+min_val for i, x in enumerate(histo) if x == max(histo) and x > 0]
    #non_zero = [[i+1, x] for i, x in enumerate(histo) if x > 0]
    #print(non_zero)
    min_found = min([x for x in histo if x > 0])
    #print("min_found = {}".format(min_found))
    min_indices = [i+min_val for i, x in enumerate(histo) if x == min_found]
    none_indices = [i+min_val for i, x in enumerate(histo) if x == 0]
    for i, ln in enumerate(histo):
        print("{:5d} ({:5d}): {}".format(min_val+i, histo[i], "+"*histo[i]))
    print("Most: {}, Least {}, None {}".format(max_indices, min_indices, none_indices))


def simple_test2(num_values=100, num_per_row=10, max_val=10, min_val=1):
    num_values = int(num_values)
    num_per_row = int(num_per_row)
    min_val = int(min_val)
    max_val = int(max_val)

    num_values = num_values if num_values >= 1 else 1
    num_per_row = num_per_row if num_per_row >= 1 else 1
    if min_val > max_val:
        tmp_val = max_val
        max_val = min_val
        min_val = tmp_val

    histo = [0 for x in range(max_val+1-min_val)]
    for i in range(num_values):
        if (i % num_per_row) == 0:
            print("{:5d}: ".format(i), end="")

        num = random.randrange(min_val, max_val+1)
        print("{:3d}, ".format(num), end="")
        histo[num-1] += 1

        if ((i+1) % num_per_row) == 0:
            print()
    # if the last thing was not a new line, add one
    if (num_values % num_per_row) != 0:
        print()
    print()

    print_histo(histo, min_val)
    print("{}\n".format("-"*79))


simple_test1()
simple_test1(5)
simple_test1(num_per_row=15)
simple_test1(5, 2)
simple_test1(max_val=20, min_val=10)
simple_test1(max_val=10, min_val=20)
simple_test1(10, max_val=15, min_val=15)

print("{}\n".format("=" * 79))

simple_test2()
simple_test2(max_val=15, num_values=15)
simple_test2(200, 10, 10, -10)

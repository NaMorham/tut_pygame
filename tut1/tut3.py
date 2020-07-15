#! /usr/bin/env python

F2C_FACTOR = 5/9
deg_c_freeze = 0.0
deg_c_boil = 100.0
deg_c_body = 37.0
deg_f_0 = 0.0
deg_f_100 = 100.0
deg_f_body = 98.6
degree_sign= u'\N{DEGREE SIGN}'


def f2c(deg_f):
    return (deg_f - 32) * F2C_FACTOR


def c2f(deg_c):
    return (deg_c / F2C_FACTOR) + 32


def c2k(deg_c):
    return deg_c + 273.15


def f2k(deg_f):
    return c2k(f2c(deg_f))


def print_val_c(label, temp_c):
    print("{:>10}: {:7.3f}{}C ==> {:7.3f}{}K ==> {:7.3f}{}F".format(label,
                                                                    temp_c, degree_sign,
                                                                    c2k(temp_c), degree_sign,
                                                                    c2f(temp_c), degree_sign))


def print_val_f(label, temp_f):
    print("{:>10}: {:7.3f}{}F ==> {:7.3f}{}K ==> {:7.3f}{}C".format(label,
                                                                    temp_f, degree_sign,
                                                                    f2k(temp_f), degree_sign,
                                                                    f2c(temp_f), degree_sign))


print_val_c("Freeze", deg_c_freeze)
print_val_c("Boil", deg_c_boil)
print_val_c("Body", deg_c_body)
print()
print_val_f("Zero", deg_f_0)
print_val_f("Hundred", deg_f_100)
print_val_f("Body", deg_f_body)
print()

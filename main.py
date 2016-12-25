from math import *

from Methods import build_graphic
from Methods import mpi

from Methods.chord import chord_method
from Methods.newton import newton_method


def derivative_func1(x):
    return 2*x + sin(2*x) + cos(x) - pow(2*sqrt(x+13), -1)


def func1(x):
    "x**2-x*cos(x)**2+sin(x)-sqrt(13+x)"
    return pow(x, 2) - pow(cos(x), 2) + sin(x) - sqrt(13+x)


def func2(x):
    return pow(x, 2) + pow(x, 3) + 35 - pow(x, 6)


def derivative_func2(x):
    return 2 * x + 3 * pow(x, 2) - 6 * pow(x, 5)


def main():
    print "Enter accuracy: "
    accuracy = float(input())
    print "Solving 4 equation by chord method: "
    c, list_of_values_root_1 = chord_method(-2.5, -1, func1, accuracy)
    print c
    c, list_of_values_rooot_2 = chord_method(1, 2, func2, accuracy)

    print "Solving 19 equation by newton method: "
    x, list_of_values2_root_1 = newton_method(-3, accuracy, func2, derivative_func2)
    x, list_of_values2_root_2 = newton_method(2, accuracy, func2, derivative_func2)
    tmp = input("Show graphic? 1 - y/ 2 - n")
    tup = ([list_of_values_root_1, "red"], [list_of_values2_root_1, "blue"])
    build_graphic.build_graphics(tup)
    tup = ([list_of_values_rooot_2, "red"], [list_of_values2_root_2, "blue"])
    build_graphic.build_graphics(tup)
    print "Solving 19 equation by method of simple iteration: "
    mpi.mpi(-3, -1, func2, derivative_func2, accuracy)
    mpi.mpi(1, 2, func2, derivative_func2, accuracy)

if __name__ == "__main__":
    main()

import math
import newton

def function(x):
    return -74 * x ** 7 - 789 * x ** 6 - 840 * x ** 5 + 907 * x ** 4 + 730 * x ** 3 - 348 * x ** 2 - 50 * x + 19


def first_derivative(x):
    return -74 * 7 * x ** 6 - 789 * 6 * x ** 5 - 840 * 5 * x ** 4 + 907 * 4 * x ** 3 + 730 * 3 * x ** 2 - 348 * 2 * x - 50


def stopping_criterion_for_newton(b, a, accuracy):
    if math.fabs(b - a) < accuracy:
        return True
    return False


def newton_method(accuracy, x_list):
    new_x_list = []
    x_list[3] -= 0.1
    for x_k in x_list:
        while True:
            x_k_1 = x_k - function(x_k) / first_derivative(x_k)
            if stopping_criterion_for_newton(x_k_1, x_k, accuracy):
                new_x_list.append(x_k_1)
                break
            x_k = x_k_1
    return new_x_list


def stopping_criterion(a_list, b_list):
    max_value = 0
    for i in range(len(a_list)):
        b = b_list[i]
        a = a_list[i] ** 2
        tmp = math.fabs(1 - float(b) / float(a))
        if tmp > max_value:
            max_value = tmp
    if max_value < 1:
        return True


def squaring(a_list):
    b_list = []
    for k in range(len(a_list)):
        sum_ = 0
        for j in range(1, len(a_list) - k):
            if ((k - j) < 0) or ((k + j) >= len(a_list)):
                break
            sum_ += a_list[k - j] * a_list[k + j] * (-1) ** j
        b_list.append(a_list[k] ** 2 + 2 * sum_)
    return b_list


def lobachevsky_method(a_list, b_list, p):
    x_list = []
    for k in range(1, len(b_list)):
        tmp = float(b_list[len(b_list) - 1 - k]) / float(b_list[len(b_list) - k])
        x = tmp ** (1.0 / (2.0 ** p))
        if (float(a_list[len(a_list) - 1 - k]) / float(a_list[len(a_list) - k])) > 0:
            x = -x
        x_list.append(x)
    return x_list


def lob():
    b_list = []
    # a_list = [-14, -288, 988, -141, -722, -67, 48, 2]
    a_list = [-74, -789, -840, 907, 730, -348, -50, 19]
    a_list.reverse()
    print a_list
    a_start_list = a_list
    count = 1
    while True:
        b_list = squaring(a_list)
        if stopping_criterion(a_list, b_list):
            break
        a_list = b_list
        count += 1
    print count
    x_list = lobachevsky_method(a_start_list, b_list, count)
    print x_list
    x_list = newton_method(0.0001, x_list)
    print x_list


lob()

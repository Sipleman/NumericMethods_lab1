import math


def lambda_(upper_bound, lower_bound):
    return 2.0 / (lower_bound + upper_bound)


def stopping_criterion(a, b, q, accuracy):
    left_side = math.fabs(b - a)
    right_side = ((1 - q) / q) * accuracy
    if left_side < right_side:
        print "|{b} - {a}| = {r} < {accur}".format(b=b, a=a, r=left_side, accur=right_side)
        return True
    print "|{b} - {a}| = {r} > {accur}".format(b=b, a=a, r=left_side, accur=right_side)
    return False


def mpi(left_border, right_border, function, first_derivative, accuracy=0.001):
    iteration = 1
    alpha = first_derivative(right_border)
    gamma = first_derivative(left_border)
    if math.fabs(alpha) > math.fabs(gamma):
        alpha, gamma = gamma, alpha
    print "Alpha = {}, gamma = {}".format(alpha, gamma)
    l = lambda_(gamma, alpha)
    print "Lambda = {}".format(l)
    q = (gamma - alpha) / (gamma + alpha)
    print "q = {}".format(q)
    x_k = left_border
    while True:
        x_k_1 = x_k - l * function(x_k)
        print "Iteration: {iter}\nx_k = {x_k}, x_k_1 = {x_k_1};".format(iter=iteration, x_k=x_k, x_k_1=x_k_1)
        if stopping_criterion(x_k, x_k_1, q, accuracy):
            print "x = {}".format(x_k_1)
            break
        x_k = x_k_1
        iteration += 1

if __name__ == '__main__':
    b = 1
    mpi(-3, -1, 0.00001)

import sympy as sym


def newton_method(x0, e, func, derivative_func):
    f = derivative_func
    print "Newton method..."
    i = 1
    list_of_values = [x0]
    while True:
        x1 = x0 - (func(x0) / f(x0))
        list_of_values.append(x1)
        print "Iteration number " + str(i)
        i += 1
        print "x1 = {x0} - (f({x0} / deriv({x0})".format(x0=x0)
        print "x1 = " + str(x1)

        if abs(x1 - x0) < e:
            print "Stopped by simplified criteria with accuracy {e}. xk+1={x1} xk={x0}".\
                format(e=e, x1=x1, x0=x0)
            print "Result: x = {x}".format(x=x1)
            return x1, list_of_values
        x0 = x1

    return list_of_values

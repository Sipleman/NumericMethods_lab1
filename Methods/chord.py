

def chord_method(a, b, func, e=0.001):
    c = a - func(a)*((b-a)/(func(b)-func(a)))
    print "Chord method"
    i = 2
    print "Iteration 1"
    print "c = {c}".format(c=c)
    list_of_values = [c]
    while e < (abs(c-a)):
        print "Iteration " + str(i)
        i += 1
        c = a - (func(a) * (b - a)) / (func(b) - func(a))
        print "c = {a} - (f({a}) * ({b} - {a}))/(f({b}) - f({a}))".format(a=a, b=b)
        print "c = {c}".format(c=c)
        a = b
        b = c
        list_of_values.append(c)

    print "Ended with accuracy e = {e}".format(e=e)
    print "Result c = {c}".format(c=c)
    return c, list_of_values

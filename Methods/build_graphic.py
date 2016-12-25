from matplotlib import pyplot as plt


def build_sub_graphic(function, a, b, color='red'):
    x_list = []
    y_list = []
    i = a
    step = 0.01
    while i <= b:
        x_list.append(i)
        y_list.append(function(i))
        i += step

    plt.plot(x_list, y_list, color=color)


def build_sub(list_of_values, color):
    y_list = []
    x_list = []
    print list_of_values
    for i in range(len(list_of_values)):
        x_list.append(i)
        y_list.append(abs(list_of_values[-1] - list_of_values[i]))

    plt.plot(x_list, y_list, color=color)


def build_coordinate_system():
    plt.plot([-100, 100], [0, 0], color='black')
    plt.plot([0, 0], [-100, 100], color='black')


def build_graphics(args):
    build_coordinate_system()
    for arg in args:
        print arg
        build_sub(arg[0], arg[1])
    plt.xlim(-5, 5)
    plt.ylim(-1, 1)
    plt.show()

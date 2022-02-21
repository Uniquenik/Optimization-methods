def f(x):
    return 2 * x * x - 12 * x  # put your function here


a = 0  # start (a_0)
b = 10  # end (b_0)
eps = 1  # epsilon (inaccuracy)
delta = 0.2  # (l) - find +-
n = 100  # limit


def dichotomy(a, b, eps, delta, n):
    a_n = a
    b_n = b
    k = -1
    while b_n - a_n > eps:
        k += 1
        x_n = (a_n + b_n - delta) / 2.0
        y_n = (a_n + b_n + delta) / 2.0
        if f(x_n) < f(y_n):
            b_n = y_n
        else:
            a_n = x_n
    print((a_n + b_n) / 2)
    print("k = " + str(k) + ", N = " + str(2 * (k + 1)))


dichotomy(a, b, eps, delta, n)

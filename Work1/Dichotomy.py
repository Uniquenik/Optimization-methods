def f(x):
    return x * x + 6 * x + 13  # put your function here


a = -6  # start (a_0)
b = 4  # end (b_0)
eps = 0.5  # epsilon (inaccuracy)
delta = 0.2  # (l) - find +-
n = 100  # limit


def dichotomy(a, b, eps, delta, n):
    a_n = a
    b_n = b
    k = -1
    while b_n - a_n > eps or n<100:
        k += 1
        x_n = (a_n + b_n - delta) / 2.0
        y_n = (a_n + b_n + delta) / 2.0
        print("Step", k)
        print("x =", x_n, ",y =", y_n)
        if f(x_n) < f(y_n):
            b_n = y_n
            print(f(x_n), "<", f(y_n))
        else:
            a_n = x_n
            print(f(x_n), ">=", f(y_n))
        print("L =[", a_n, ";", b_n, "] and", eps)
    print("\nAnswer:", (a_n + b_n) / 2)
    print("k =", k, ", N =", 2 * (k + 1))


dichotomy(a, b, eps, delta, n)

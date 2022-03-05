def f(x):
    return x * x + 6 * x + 13  # put your function here


a = -6  # start (a_0)
b = 4  # end (b_0)
l = 0.2  # (l) - find +-
n = 100  # limit


def golden_section(a, b, l, n):
    a_n = a
    b_n = b
    k = -1
    while b_n - a_n > l or n < 100:
        k += 1
        y_n = a_n + 0.381966 * (b_n - a_n)
        z_n = a_n + b_n - y_n
        print("Step", k)
        print("y =", y_n, ",z =", z_n)
        if f(y_n) > f(z_n):
            print(f(y_n), ">", f(z_n))
            a_n = y_n
            y_n = z_n
            z_n = a_n + b_n - z_n
        else:
            print(f(y_n), "<=", f(z_n))
            b_n = z_n
            z_n = y_n
            y_n = a_n + b_n - y_n
        print("L = [", a_n, ";", b_n, "] and", l)
    print("\nAnswer:", (a_n + b_n) / 2)
    print("k =", k, ", N =", 2 * (k + 1))


golden_section(a, b, l, n)
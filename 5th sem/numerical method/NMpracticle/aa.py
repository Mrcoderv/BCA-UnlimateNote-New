def func(x):
    return x*x*x - x*x + 2


def bisection(a, b, epsilon=0.01):

    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return

    print(f"{'Iter':<5}{'a':<12}{'b':<12}{'c':<12}{'f(c)':<12}")
    print("-" * 53)

    iteration = 1

    while (b - a) >= epsilon:

        c = (a + b) / 2

        print(f"{iteration:<5}{a:<12.4f}{b:<12.4f}{c:<12.4f}{func(c):<12.4f}")

        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iteration += 1

    print("\nThe value of root is :", "%.4f" % c)


# Driver code
a = -200
b = 300
bisection(a, b)

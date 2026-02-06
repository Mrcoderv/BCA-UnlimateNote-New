import math
def f(x):
    return x * math.exp(x) - math.cos(x)
a, b = 0.0, 1.0

print("Iter |    a     |    b     |    m     |   f(m)")
print("------------------------------------------------")

for i in range(1, 12):
    m = (a + b) / 2
    print(f"{i:4d} | {a:8.4f} | {b:8.4f} | {m:8.4f} | {f(m):8.4f}")

    if f(a) * f(m) < 0:
        b = m
    else:
        a = m

print("\nThe approximate root is", round(m, 4))

#Use the Bisection Method to compute a
# root of the equation: x * e ^ x = cosx correct to 4 decimal places
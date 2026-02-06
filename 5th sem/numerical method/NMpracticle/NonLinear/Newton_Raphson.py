def newton_raphson(f, df, x, tol=0.001, n=100):
    print("Iter |    x     |   f(x)   |  f'(x)  |  Error")
    print("-----------------------------------------------")

    for i in range(n+1):
        fx, dfx = f(x), df(x)
        x_new = x - fx / dfx
        error = abs(x_new - x)

        print(f"{i + 1:4d} | {x:8.4f} | {fx:8.4f} | {dfx:8.4f} | {error:7.4f}")

        if error < tol:
            fx_new, dfx_new = f(x_new), df(x_new)
            print(f"{i + 2:4d} | {x_new:8.4f} | {fx_new:8.4f} | {dfx_new:8.4f} | {0.0:7.4f}")
            return x_new
        x = x_new

    return x


f = lambda x: x ** 3 - 2 * x - 5
df = lambda x: 3 * x ** 2 - 2

root = newton_raphson(f, df, 2.0)
print(f"\nApproximate root = {root:.3f}")


#Find the root of the equation  is x^3 -2x =5 correct up to three decimaL  .

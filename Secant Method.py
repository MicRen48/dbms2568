def myRun():
    print("Welcome to CDTI68's Nonlinear Equation Solver")
    print("(1) Secant Method")
    print("(2) Newton-Raphson method")

    choice = int(input("Your choice (1 or 2): "))

    s = input("Input your f(x) using correct Python expression: ")
    f = lambda x: eval(s)

    if choice == 2:
        ds = input("Input f'(x) using correct Python expression: ")
        df = lambda x: eval(ds)

        def CalM(E):
            m, T = 0, 5
            while T >= E:
                m += 1
                T /= 10
            return m

        def newton(x0):
            print(f"\nSolving the nonlinear equation {s}")
            print("using the newton-raphson method.")
            print("="*60)
            print(f" i|{'x0':^8}|{'x1':^8}|{'f(x1)':^13}|{'Ea':^12}|{'m'}")
            print("="*60)

            for i in range(1, 20):
                x1 = x0 - f(x0)/df(x0)
                Ea = abs((x1-x0)/x1)*100
                m = CalM(Ea)
                print(f"{i:2d}|{x0:8.5f}|{x1:8.5f}|{f(x1):13.6e}|{Ea:13.6e}|{m}")
                x0 = x1
                if m >= 8:
                    break

        x0 = float(input("Input x0: "))
        newton(x0)

if __name__ == '__main__':
    myRun()

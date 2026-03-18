def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = ext_gcd(b, a % b)
    return g, y, x - (a // b) * y


def main():
    a = int(input("a: "))
    b = int(input("b: "))
    g, x, y = ext_gcd(a, b)
    print("gcd:", g)
    print("x:", x)
    print("y:", y)


if __name__ == "__main__":
    main()

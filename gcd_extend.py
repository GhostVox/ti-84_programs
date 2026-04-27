def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = ext_gcd(b, a % b)
    return g, y, x - (a // b) * y


inverse = 0
a = int(input("a: "))
b = int(input("b: "))
g, x, y = ext_gcd(a, b)
if g == 1:
    inverse = x % b
elif (x * a) % b == 1:
    inverse = x
elif (y * a) % b == 1:
    inverse = y
else:
    inverse = "None"
print("gcd:", g)
print("x:", x)
print("y:", y)
print("inverse:", inverse)

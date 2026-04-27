base = int(input("Enter the base:"))
exponent = int(input("Enter the exponent:"))
mod = int(input("Enter the modulus:"))
result = 1
base = base % mod
while exponent > 0:
    if exponent % 2 == 1:
        result = (result * base) % mod
    exponent = exponent // 2
    base = (base * base) % mod
print(result)

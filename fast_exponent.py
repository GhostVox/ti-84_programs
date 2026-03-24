def fast_mod_pow(base, exp, mod):
    result = 1
    base = base % mod  # Initial reduction

    while exp > 0:
        # If the current bit is 1, multiply the result
        if exp % 2 == 1:
            result = (result * base) % mod

        # Square the base for the next bit
        base = (base * base) % mod

        # Shift the exponent right by 1 bit (integer division by 2)
        exp //= 2

    return result


# Usage
base = int(input("Enter:base"))
exponent = int(input("Enter exponent"))
mod = int(input("Enter modulos"))
print(fast_mod_pow(base, exponent, mod))  # Output: 644

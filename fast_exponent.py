def main():
    base = int(input("Enter the base: "))
    exp = int(input("Enter the exponent: "))
    mod = int(input("Enter the modulus: "))

    # Reverse the string so bin_rep[0] is the 2^0 bit
    bin_rep = bin(exp)[2:][::-1]

    results = {}
    # 1. Square Phase
    for i in range(len(bin_rep)):
        if i == 0:
            results[i] = base % mod
        else:
            results[i] = (results[i - 1] ** 2) % mod

    # 2. Multiply Phase
    running_mul = 1
    for i in range(len(bin_rep)):
        if bin_rep[i] == "1":
            # Multiply and Modulo immediately to prevent overflow
            running_mul = (running_mul * results[i]) % mod
            print(
                f"Multiplying by {base}^{2**i} ({results[i]}), Current: {running_mul}"
            )

    print(f"\nResult: {running_mul}")


if __name__ == "__main__":
    main()

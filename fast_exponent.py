def main():

    base = int(input("Enter the base: "))
    exp = int(input("Enter the exponent: "))
    mod = int(input("Enter the modulus: "))
    bin_rep = bin(exp)[2:]
    print(bin_rep)
    runs = len(bin_rep)
    results: dict[int, int] = dict()

    for i in range(runs):
        if i == 0:
            results[i] = base % mod
        else:
            last_mod = results.get(i - 1, base)
            curr_mod = (last_mod * last_mod) % mod
            results[i] = curr_mod

    running_mul = 1
    for i in range(runs - 1, -1, -1):
        if bin_rep[i] == "1":
            print(f"Multiplying by {results.get(i, base)}")
            running_mul = running_mul * results.get(i, base)

    print(f"{base}^{exp} mod {mod} = {running_mul % mod}")


if __name__ == "__main__":
    main()

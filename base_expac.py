def main():

    def recursive_expac(string: str, base: int, n: int) -> None:
        div_result: int = n // base
        mod_result: int = n % base
        if div_result == 0:
            print(f"{mod_result}{string}")
            return
        string = f"{mod_result}{string}"
        recursive_expac(string, base, div_result)

    print("Enter base:")
    base = int(input())

    if base < 2:
        print("Base must be at least 2.")
        return
    print("Enter n:")
    n = int(input())
    if n < 0:
        print("n must be non-negative.")
        return

    recursive_expac("", base, n)


if __name__ == "__main__":
    main()

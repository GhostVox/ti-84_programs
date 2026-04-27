num = input("Enter a binary number: ")
result = 0
place_val = 0
len = len(num) - 1
while len >= 0:
    if num[len] == "1":
        result += 2**place_val
    place_val += 1
    len -= 1
print(result)

def largest_12_digits(bank):
    k = 12
    to_remove = len(bank) - k
    stack = []

    for digit in bank:
        while stack and to_remove > 0 and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    # If stack still has extra digits, cut it down
    return "".join(stack[:k])


if __name__ == "__main__":
    banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111"
    ]
    file = open('day3input.txt')
    banks = file.read().split('\n')[:-1]
    file.close()
    results = []
    total = 0

    for b in banks:
        out = int(largest_12_digits(b))
        print(out)
        results.append(out)
        total += out

    print("Total:", total)

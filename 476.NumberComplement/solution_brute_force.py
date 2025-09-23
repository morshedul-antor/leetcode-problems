# Time-Complexity: O(log n)
# Space-Complexity: O(log n)


def number_complement(num: int) -> int:
    binary = bin(num)[2:]
    value = ""

    for num in binary:
        if num == "0":
            value += "1"
        else:
            value += "0"

    return int(value, 2)


def run_tests():
    assert number_complement(num=5) == 2
    assert number_complement(num=1) == 0
    assert number_complement(num=7) == 0
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

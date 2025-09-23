# Time-Complexity: O(log n)
# Space-Complexity: O(1)


def number_complement(num: int) -> int:
    if num == 0:
        return 1

    mask = (1 << num.bit_length()) - 1

    return num ^ mask


def run_tests():
    assert number_complement(num=5) == 2
    assert number_complement(num=1) == 0
    assert number_complement(num=7) == 0
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

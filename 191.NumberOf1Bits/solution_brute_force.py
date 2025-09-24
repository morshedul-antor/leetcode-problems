# Time-Complexity: O(log n)
# Space-Complexity: O(log n)


def number_of_bits(n: int) -> int:
    binary = bin(n)[2:]
    count = 0

    for bit in binary:
        if bit == "1":
            count += 1

    return count


def run_tests():
    assert number_of_bits(n=11) == 3
    assert number_of_bits(n=128) == 1
    assert number_of_bits(n=2147483645) == 30
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

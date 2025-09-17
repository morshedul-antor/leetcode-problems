# Time-Complexity: O(n)
# Space-Complexity: O(n)


def number_of_segments(s):
    s = s.split()

    return len(s)


def run_tests():
    assert number_of_segments(s="Hello, my name is John") == 5
    assert number_of_segments(s="Hello") == 1
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

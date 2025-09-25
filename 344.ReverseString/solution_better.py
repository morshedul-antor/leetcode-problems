# Time-Complexity: O(n)
# Space-Complexity: O(n)


def reverse_string(s):
    return s[::-1]


def run_tests():
    assert reverse_string(
        s=["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
    assert reverse_string(
        s=["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"]
    assert reverse_string(s=["a", "c"]) == ["c", "a"]
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

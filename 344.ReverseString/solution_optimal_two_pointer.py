# Time-Complexity: O(n)
# Space-Complexity: O(1)


def reverse_string(s):
    left = 0
    right = len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

    return s


def run_tests():
    assert reverse_string(
        s=["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
    assert reverse_string(
        s=["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"]
    assert reverse_string(s=["a", "c"]) == ["c", "a"]
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

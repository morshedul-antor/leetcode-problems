# Time-Complexity: O(n log n)
# Space-Complexity: O(n)


def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s = sorted(s)
    t = sorted(t)

    return s == t


def run_tests():
    assert valid_anagram(s="anagram", t="nagaram") == True
    assert valid_anagram(s="rat", t="car") == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

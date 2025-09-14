# Time-Complexity: O(n)
# Space-Complexity: O(n)


def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1

        if char_count[char] < 0:
            return False

    return True


def run_tests():
    assert valid_anagram(s="anagram", t="nagaram") == True
    assert valid_anagram(s="rat", t="car") == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

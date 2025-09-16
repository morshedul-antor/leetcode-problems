# Time-Complexity: O(n)
# Space-Complexity: O(n)


def reverse_vowels(s):
    vowels = set("aeiouAEIOU")
    s = list(s)

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)


def run_tests():
    assert reverse_vowels(s="IceCreAm") == "AceCreIm"
    assert reverse_vowels(s="leetcode") == "leotcede"
    assert reverse_vowels(s="race car") == "race car"
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

# Time-Complexity: O(n)
# Space-Complexity: O(1)


def first_unique_character(s):
    freq = [0] * 26

    for char in s:
        freq[ord(char) - ord('a')] += 1

    for i in range(len(s)):
        if freq[ord(s[i]) - ord('a')] == 1:
            return i

    return -1


def run_tests():
    assert first_unique_character(s="leetcode") == 0
    assert first_unique_character(s="loveleetcode") == 2
    assert first_unique_character(s="aabb") == -1
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

# Time-Complexity: O(n)
# Space-Complexity: O(1)


def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s = [0] * 26
    count_t = [0] * 26

    for i in range(len(s)):
        count_s[ord(s[i]) - ord('a')] += 1
        count_t[ord(t[i]) - ord('a')] += 1

    return count_s == count_t

    # freq = [0] * 26
    # for i in range(len(s)):
    #     freq[ord(s[i]) - ord('a')] += 1
    #     freq[ord(t[i]) - ord('a')] -= 1

    # for i in range(len(freq)):
    #     if freq[i] != 0:
    #         return False
    # return True


def run_tests():
    assert valid_anagram(s="anagram", t="nagaram") == True
    assert valid_anagram(s="rat", t="car") == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

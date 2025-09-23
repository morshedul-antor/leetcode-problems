# Time-Complexity: O(n+m)
# Space-Complexity: O(m)


def word_pattern(pattern: str, s: str) -> bool:
    s = s.split()
    seen = {}
    words = set()

    if len(pattern) != len(s):
        return False

    for i, val in enumerate(pattern):
        if val in seen:
            if seen[val] != s[i]:
                return False
        else:
            if s[i] in words:
                return False

            seen[val] = s[i]
            words.add(s[i])

    return True


def run_tests():
    assert word_pattern(pattern="abba", s="dog cat cat dog") == True
    assert word_pattern(pattern="abba", s="dog cat cat fish") == False
    assert word_pattern(pattern="aaaa", s="dog cat cat dog") == False
    assert word_pattern(pattern="abba", s="dog dog dog dog") == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

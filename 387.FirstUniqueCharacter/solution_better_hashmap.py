# Time-Complexity: O(n)
# Space-Complexity: O(n)


def first_unique_character(s):
    hashmap = {}

    for char in s:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1

    for i in range(len(s)):
        if hashmap[s[i]] == 1:
            return i

    return -1


def run_tests():
    assert first_unique_character(s="leetcode") == 0
    assert first_unique_character(s="loveleetcode") == 2
    assert first_unique_character(s="aabb") == -1
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

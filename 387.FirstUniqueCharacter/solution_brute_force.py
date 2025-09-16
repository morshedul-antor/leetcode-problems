# Time-Complexity: O(n^2)
# Space-Complexity: O(1)


def first_unique_character(s):
    for i in range(len(s)):
        counter = 0

        for j in range(len(s)):
            if s[i] == s[j]:
                counter += 1

                if counter > 1:
                    break

        if counter == 1:
            return i

    return -1


def run_tests():
    assert first_unique_character(s="leetcode") == 0
    assert first_unique_character(s="loveleetcode") == 2
    assert first_unique_character(s="aabb") == -1
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

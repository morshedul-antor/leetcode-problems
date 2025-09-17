# Time-Complexity: O(n)
# Space-Complexity: O(1)


def number_of_segments(s):
    count = 0

    for i in range(len(s)):
        # not space and either first character or comes after a space
        if s[i] != " " and (i == 0 or s[i-1] == " "):
            count += 1

    return count


def run_tests():
    assert number_of_segments(s="Hello, my name is John") == 5
    assert number_of_segments(s="Hello") == 1
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

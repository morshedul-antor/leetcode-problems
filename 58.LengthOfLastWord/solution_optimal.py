# Time-Complexity: O(n)
# Space-Complexity: O(1)


def lenth_of_last_word(s: str) -> int:
    count = 0

    for i in range(len(s)-1, -1, -1):
        if s[i] != " ":
            count += 1
        else:
            if count > 0:
                return count

    return -1


def run_tests():
    assert lenth_of_last_word(s="Hello World") == 5  # "World"
    assert lenth_of_last_word(s="   fly me   to   the moon  ") == 4  # "moon"
    assert lenth_of_last_word(s="luffy is still joyboy") == 6  # "joyboy"
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

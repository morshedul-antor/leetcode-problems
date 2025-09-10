# Time-Complexity: O(n)
# Space-Complexity: O(n)


def lenth_of_last_word(s: str) -> int:
    s = s.strip()
    s = s.split(" ")

    return len(s[-1])


def run_tests():
    assert lenth_of_last_word(s="Hello World") == 5  # "World"
    assert lenth_of_last_word(s="   fly me   to   the moon  ") == 4  # "moon"
    assert lenth_of_last_word(s="luffy is still joyboy") == 6  # "joyboy"
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

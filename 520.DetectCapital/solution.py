# Time-Complexity: O(n)
# Space-Complexity: O(1)


def detect_capital(word: str) -> bool:
    upper = 0
    lower = 0

    for i, char in enumerate(word):
        if i == 0 and char.isupper():
            continue

        if char.isupper():
            upper += 1
        else:
            lower += 1

    if upper and lower:
        return False

    return True


def run_tests():
    assert detect_capital(word="USA") == True
    assert detect_capital(word="FlaG") == False
    assert detect_capital(word="g") == True
    assert detect_capital(word="Leetcode") == True
    assert detect_capital(word="mL") == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

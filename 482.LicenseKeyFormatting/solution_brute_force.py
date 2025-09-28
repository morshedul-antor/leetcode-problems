# Time-Complexity: O(n)
# Space-Complexity: O(n)


def license_key_formatting(s: str, k: int) -> str:
    count = 0
    word = []
    res = ""

    for i in range(len(s)):
        if s[i] != "-":
            word.append(s[i])

    for i in range(len(word)-1, -1, -1):
        res = word[i].upper() + res
        count += 1

        if i != 0 and count == k:
            res = "-" + res
            count = 0

    return res


def run_tests():
    assert license_key_formatting(s="5F3Z-2e-9-w", k=4) == "5F3Z-2E9W"
    assert license_key_formatting(s="2-5g-3-J", k=2) == "2-5G-3J"
    assert license_key_formatting(s="--a-a-a-a--", k=2) == "AA-AA"
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

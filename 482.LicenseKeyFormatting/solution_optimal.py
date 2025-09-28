# Time-Complexity: O(n)
# Space-Complexity: O(n)


def license_key_formatting(s: str, k: int) -> str:
    s = "".join(ch for ch in s if ch != "-").upper()
    size = len(s)

    first = size % k or k
    groups = [s[:first]]

    for i in range(first, size, k):
        groups.append(s[i:i+k])

    return "-".join(groups)


def run_tests():
    assert license_key_formatting(s="5F3Z-2e-9-w", k=4) == "5F3Z-2E9W"
    assert license_key_formatting(s="2-5g-3-J", k=2) == "2-5G-3J"
    assert license_key_formatting(s="--a-a-a-a--", k=2) == "AA-AA"
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

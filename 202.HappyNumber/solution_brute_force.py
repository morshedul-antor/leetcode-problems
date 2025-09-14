# Time-Complexity: O(log n)
# Space-Complexity: O(n)


def happy_number(n: int) -> bool:
    hashset = set()

    while n != 1 and n not in hashset:
        hashset.add(n)
        result = 0

        while n > 0:
            result += (n % 10)**2
            n = n // 10
        n = result

    return n == 1


def run_tests():
    assert happy_number(n=19) == True
    assert happy_number(n=2) == False
    assert happy_number(n=7) == True
    assert happy_number(n=116) == False
    assert happy_number(n=4) == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

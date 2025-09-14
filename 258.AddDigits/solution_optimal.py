# Time-Complexity: O(1)
# Space-Complexity: O(1)


def add_digits(num: int) -> int:
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9


def run_tests():
    assert add_digits(num=38) == 2  # 3+8=11 -> 1+1=2
    assert add_digits(num=0) == 0
    assert add_digits(num=121) == 4
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

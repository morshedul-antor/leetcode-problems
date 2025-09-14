# Time-Complexity: O(log n)
# Space-Complexity: O(1)


def add_digits(num: int) -> int:
    result = 0

    while num > 0:
        result += num % 10
        num = num // 10

        if result > 9 and num == 0:
            num = result
            result = 0

    return result


def run_tests():
    assert add_digits(num=38) == 2  # 3+8=11 -> 1+1=2
    assert add_digits(num=0) == 0
    assert add_digits(num=121) == 4
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

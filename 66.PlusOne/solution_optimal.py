# Time-Complexity: O(n)
# Space-Complexity: O(1)


def plus_one(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    return [1] + digits  # if all digits are 9


def run_tests():
    assert plus_one(digits=[1, 2, 3]) == [1, 2, 4]
    assert plus_one(digits=[4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plus_one(digits=[9]) == [1, 0]
    assert plus_one(digits=[9, 9]) == [1, 0, 0]
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

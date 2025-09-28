# Time-Complexity: O(n)
# Space-Complexity: O(n)


def plus_one(digits):
    res = []
    nums = ""

    for num in digits:
        nums += str(num)

    nums = str(int(nums) + 1)

    for num in nums:
        res.append(int(num))

    return res


def run_tests():
    assert plus_one(digits=[1, 2, 3]) == [1, 2, 4]
    assert plus_one(digits=[4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plus_one(digits=[9]) == [1, 0]
    assert plus_one(digits=[99]) == [1, 0, 0]
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

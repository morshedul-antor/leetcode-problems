# Time-Complexity: O(n)
# Space-Complexity: O(1)


def max_consecutive_ones(nums):
    left = 0
    res = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            left = right + 1

        length = right - left + 1

        if length > res:
            res = length

    return res


def run_tests():
    assert max_consecutive_ones(nums=[1, 1, 0, 1, 1, 1]) == 3
    assert max_consecutive_ones(nums=[1, 0, 1, 1, 0, 1]) == 2
    assert max_consecutive_ones(nums=[1, 0, 1, 1, 1, 1, 0, 1]) == 4
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

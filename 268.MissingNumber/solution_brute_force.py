# Time-Complexity: O(n log n)
# Space-Complexity: O(n)


def missing_number(nums):
    nums = sorted(nums)

    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] != 1:
            return nums[i]-1

    return len(nums)


def run_tests():
    assert missing_number(nums=[3, 0, 1]) == 2
    assert missing_number(nums=[0, 1]) == 2
    assert missing_number(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

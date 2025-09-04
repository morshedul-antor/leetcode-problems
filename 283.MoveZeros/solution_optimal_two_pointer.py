# Time-Complexity: O(n)
# Space-Complexity: O(1)


def move_zeroes(nums):
    last_non_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1
    return nums


def run_tests():
    assert move_zeroes(nums=[0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zeroes(nums=[0, 3, 0]) == [3, 0, 0]
    assert move_zeroes(nums=[3, 5, 0]) == [3, 5, 0]
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

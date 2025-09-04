# Time-Complexity: O(n)
# Space-Complexity: O(n)


def move_zeroes(nums):
    array_relative = []
    array_zero = []

    for i in range(len(nums)):
        if nums[i] != 0:
            array_relative.append(nums[i])
        else:
            array_zero.append(nums[i])

    return array_relative + array_zero


def run_tests():
    assert move_zeroes(nums=[0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zeroes(nums=[0, 3, 0]) == [3, 0, 0]
    assert move_zeroes(nums=[3, 5, 0]) == [3, 5, 0]
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

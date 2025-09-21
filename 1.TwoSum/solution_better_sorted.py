# Time-Complexity: O(n)
# Space-Complexity: O(1) -- if the array is sorted


def two_sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] == target:
            return [left, right]
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1
    return -1


def run_tests():
    assert two_sum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert two_sum(nums=[3, 3], target=6) == [0, 1]
    assert two_sum(nums=[3, 5], target=6) == -1
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

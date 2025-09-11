# Time-Complexity: O(n log n)
# Space-Complexity: O(1)


def contains_duplicate(nums):
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False


def run_tests():
    assert contains_duplicate(nums=[1, 2, 3, 1]) == True
    assert contains_duplicate(nums=[1, 2, 3, 4]) == False
    assert contains_duplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

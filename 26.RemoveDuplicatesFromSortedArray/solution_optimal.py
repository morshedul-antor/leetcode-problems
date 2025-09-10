# Time-Complexity: O(n)
# Space-Complexity: O(1)


def remove_duplicates(nums: list):
    count = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[count] = nums[i]
            count += 1

    return count


def run_tests():
    assert remove_duplicates(nums=[1, 1, 2]) == 2  # nums = [1, 2, '_']
    assert remove_duplicates(
        nums=[1, 2, 2, 3, 3]) == 3  # nums = [1, 2, 3, '_', '_']
    assert remove_duplicates(
        nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5  # nums [0, 1, 2, 3, 4, '_', '_', '_', '_', '_']
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

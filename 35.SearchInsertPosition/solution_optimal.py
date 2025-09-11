# Time-Complexity: O(log n)
# Space-Complexity: O(1)


def search_insert_position(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left+right)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left


def run_tests():
    assert search_insert_position(nums=[1, 3, 5, 6], target=5) == 2
    assert search_insert_position(nums=[1, 3, 5, 6], target=2) == 1
    assert search_insert_position(nums=[1, 3, 5, 6], target=7) == 4
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

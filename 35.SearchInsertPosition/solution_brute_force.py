# Time-Complexity: O(n)
# Space-Complexity: O(1)


def search_insert_position(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i

    return len(nums)


def run_tests():
    assert search_insert_position(nums=[1, 3, 5, 6], target=5) == 2
    assert search_insert_position(nums=[1, 3, 5, 6], target=2) == 1
    assert search_insert_position(nums=[1, 3, 5, 6], target=7) == 4
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

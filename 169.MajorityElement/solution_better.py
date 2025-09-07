# Time-Complexity: O(n log n)
# Space-Complexity: O(n) -- if majority element is guaranteed


def majority_element(nums):
    sorted_nums = sorted(nums)
    mid = len(nums)//2

    return sorted_nums[mid]


def run_tests():
    assert majority_element(nums=[3, 2, 3]) == 3
    assert majority_element(nums=[2, 2, 1, 1, 1, 2, 2]) == 2
    assert majority_element(nums=[3, 5, 5, 4, 5]) == 5
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

# Time-Complexity: O(n^2)
# Space-Complexity: O(1)


def majority_element(nums):
    size = len(nums)

    for i in range(size):
        counter = 1

        for j in range(i+1, size):
            if nums[j] == nums[i]:
                counter += 1

        if counter > size//2:
            return nums[i]

    return -1


def run_tests():
    assert majority_element(nums=[3, 2, 3]) == 3
    assert majority_element(nums=[2, 2, 1, 1, 1, 2, 2]) == 2
    assert majority_element(nums=[3, 5, 5, 4, 5]) == 5
    assert majority_element(nums=[3, 5, 4, 5]) == -1
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

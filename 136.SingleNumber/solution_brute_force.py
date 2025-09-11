# Time-Complexity: O(n^2)
# Space-Complexity: O(1)


def single_number(nums):
    for i in range(len(nums)):
        count = 0

        for j in range(len(nums)):
            if nums[i] == nums[j]:
                count += 1

        if count == 1:
            return nums[i]

    return -1


def run_tests():
    assert single_number(nums=[2, 2, 1]) == 1
    assert single_number(nums=[4, 1, 2, 1, 2]) == 4
    assert single_number(nums=[1]) == 1
    assert single_number(nums=[3, 5, 5]) == 3
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

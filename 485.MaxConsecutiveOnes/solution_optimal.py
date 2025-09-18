# Time-Complexity: O(n)
# Space-Complexity: O(1)


def max_consecutive_ones(nums):
    count = 0
    res = 0

    for num in nums:
        if num == 1:
            count += 1
        else:
            count = 0

        if count > res:
            res = count

    return res


def run_tests():
    assert max_consecutive_ones(nums=[1, 1, 0, 1, 1, 1]) == 3
    assert max_consecutive_ones(nums=[1, 0, 1, 1, 0, 1]) == 2
    assert max_consecutive_ones(nums=[1, 0, 1, 1, 1, 1, 0, 1]) == 4
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

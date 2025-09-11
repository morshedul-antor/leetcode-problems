# Time-Complexity: O(n)
# Space-Complexity: O(1)


def single_number(nums):
    results = 0

    for num in nums:
        results ^= num

    return results


def run_tests():
    assert single_number(nums=[2, 2, 1]) == 1
    assert single_number(nums=[4, 1, 2, 1, 2]) == 4
    assert single_number(nums=[1]) == 1
    assert single_number(nums=[3, 5, 5]) == 3
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

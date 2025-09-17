# Time-Complexity: O(n)
# Space-Complexity: O(1)


def missing_number(nums):
    n = len(nums)
    xor = 0

    for i in range(n+1):
        xor ^= i

    for num in nums:
        xor ^= num

    return xor


def run_tests():
    assert missing_number(nums=[3, 0, 1]) == 2
    assert missing_number(nums=[0, 1]) == 2
    assert missing_number(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

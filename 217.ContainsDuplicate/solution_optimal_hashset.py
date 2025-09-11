# Time-Complexity: O(n)
# Space-Complexity: O(n)


def contains_duplicate(nums):
    hashset = set()

    for num in nums:
        if num in hashset:
            return True

        hashset.add(num)

    return False


def run_tests():
    assert contains_duplicate(nums=[1, 2, 3, 1]) == True
    assert contains_duplicate(nums=[1, 2, 3, 4]) == False
    assert contains_duplicate(nums=[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

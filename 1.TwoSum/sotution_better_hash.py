# Time-Complexity: O(n)
# Space-Complexity: O(n)

def two_sum(nums, target):
    hash_map = {}

    for i in range(len(nums)):
        current_diff = target - nums[i]

        if current_diff in hash_map:
            return [hash_map[current_diff], i]
        hash_map[nums[i]] = i

    return -1


def run_tests():
    assert two_sum(nums=[2, 7, 11, 15], target=9) == [0, 1]
    assert two_sum(nums=[3, 2, 4], target=6) == [1, 2]
    assert two_sum(nums=[3, 3], target=6) == [0, 1]
    assert two_sum(nums=[3, 5], target=6) == -1
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

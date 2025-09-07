# Time-Complexity: O(n)
# Space-Complexity: O(n)


def majority_element(nums):
    hashmap = {}

    for num in nums:
        # hashmap[num] = hashmap.get(num, 0) + 1 -- can be used instead of [if else] below
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1

    for i in hashmap:
        if hashmap[i] > len(nums)//2:
            return i

    return -1


def run_tests():
    assert majority_element(nums=[3, 2, 3]) == 3
    assert majority_element(nums=[2, 2, 1, 1, 1, 2, 2]) == 2
    assert majority_element(nums=[3, 5, 5, 4, 5]) == 5
    assert majority_element(nums=[3, 5, 4, 5]) == -1
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

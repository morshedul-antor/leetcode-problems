# Time-Complexity: O(n)
# Space-Complexity: O(n)


def single_number(nums):
    hashmap = {}

    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1

    for i in hashmap:
        if hashmap[i] == 1:
            return i

    return -1


def run_tests():
    assert single_number(nums=[2, 2, 1]) == 1
    assert single_number(nums=[4, 1, 2, 1, 2]) == 4
    assert single_number(nums=[1]) == 1
    assert single_number(nums=[3, 5, 5]) == 3
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

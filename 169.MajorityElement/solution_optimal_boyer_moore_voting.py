# Time-Complexity: O(n)
# Space-Complexity: O(1)


def majority_element(nums):
    counter = 0
    element = 0

    for num in nums:
        if counter == 0:
            element = num
            counter += 1
        elif num == element:
            counter += 1
        else:
            counter -= 1

    count = 0
    for num in nums:
        if num == element:
            count += 1

        if count > len(nums)//2:
            return element

    return -1


def run_tests():
    assert majority_element(nums=[3, 2, 3]) == 3
    assert majority_element(nums=[2, 2, 1, 1, 1, 2, 2]) == 2
    assert majority_element(nums=[3, 5, 5, 4, 5]) == 5
    assert majority_element(nums=[3, 5, 4, 5]) == -1
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

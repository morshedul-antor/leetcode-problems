# Time-Complexity: O(n)
# Space-Complexity: O(n)


def remove_element(nums: list, val: int):
    store_val = []
    store = []

    for num in nums:
        if num == val:
            store_val.append('_')
        else:
            store.append(num)

    return len(store), store + store_val


def run_tests():
    assert remove_element(nums=[3, 2, 2, 3], val=3) == (2, [2, 2, '_', '_'])
    assert remove_element(nums=[3, 2, 2, 3, 1], val=2) == (
        3, [3, 3, 1, '_', '_'])
    assert remove_element(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2) == (
        5, [0, 1, 3, 0, 4, '_', '_', '_'])
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

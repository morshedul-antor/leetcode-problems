# Time-Complexity: O(n)
# Space-Complexity: O(n)


def remove_duplicates(nums: list):
    store = []
    store_duplicate = []

    for num in nums:
        if num not in store:
            store.append(num)
        else:
            store_duplicate.append('_')

    return len(store), store + store_duplicate


def run_tests():
    assert remove_duplicates(nums=[1, 1, 2]) == (2, [1, 2, '_'])
    assert remove_duplicates(nums=[3, 2, 2, 3, 1]) == (
        3, [3, 2, 1, '_', '_'])
    assert remove_duplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == (
        5, [0, 1, 2, 3, 4, '_', '_', '_', '_', '_'])
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

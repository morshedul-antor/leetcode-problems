# Time-Complexity: O((n + m) log(n + m))
# Space-Complexity: O(n + m)


def merge_two_sorted_lists(list1, list2):
    list = list1 + list2

    if len(list) != 0:
        return sorted(list)

    return list


def run_tests():
    assert merge_two_sorted_lists(
        list1=[1, 2, 4], list2=[1, 3, 4]) == [1, 1, 2, 3, 4, 4]
    assert merge_two_sorted_lists(list1=[], list2=[]) == []
    assert merge_two_sorted_lists(list1=[], list2=[0]) == [0]
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

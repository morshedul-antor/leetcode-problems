# Time-Complexity: O()
# Space-Complexity: O()


def remove_element(nums: list, val: int):
    count = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1

    return count


def run_tests():
    assert remove_element(nums=[3, 2, 2, 3], val=3) == 2  # nums = [2,2,_,_]
    assert remove_element(
        nums=[3, 2, 2, 3, 1], val=2) == 3  # nums = [3,3,1,_,_]
    assert remove_element(
        nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2) == 5  # nums = [0,1,3,0,4_,_]
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

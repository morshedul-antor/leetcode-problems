# Time-Complexity: O(log n)
# Space-Complexity: O(1)


def power_of_three(num):
    if num < 1:
        return False

    left = 0
    right = (num//2) + 1

    while left <= right:
        mid = (left+right) // 2

        if 3 ** mid == num:
            return True
        elif 3 ** mid > num:
            right = mid - 1
        else:
            left = mid + 1

    return False


def run_tests():
    assert power_of_three(num=27) == True
    assert power_of_three(num=81) == True
    assert power_of_three(num=36) == False
    assert power_of_three(num=0) == False
    assert power_of_three(num=-1) == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

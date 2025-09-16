# Time-Complexity: O(log n)
# Space-Complexity: O(1)


def power_of_three(num):
    if num < 1:
        return False

    i = 1
    # while 3**i < num:
    #     i += 1
    # return 3**i == num

    while i < num:
        i *= 3

    return i == num


def run_tests():
    assert power_of_three(num=27) == True
    assert power_of_three(num=81) == True
    assert power_of_three(num=36) == False
    assert power_of_three(num=0) == False
    assert power_of_three(num=-1) == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

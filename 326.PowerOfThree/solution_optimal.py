# Time-Complexity: O(1)
# Space-Complexity: O(1)


def power_of_three(num):
    # largest power of 3, that fits in a 32-bit is 20 [<= 2^31-1]
    return num > 0 and (3**20 % num) == 0


def run_tests():
    assert power_of_three(num=27) == True
    assert power_of_three(num=81) == True
    assert power_of_three(num=36) == False
    assert power_of_three(num=0) == False
    assert power_of_three(num=-1) == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

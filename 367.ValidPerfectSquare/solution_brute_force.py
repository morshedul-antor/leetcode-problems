# Time-Complexity: O(√n)
# Space-Complexity: O(1)


def valid_perfect_square(num):
    i = 1

    # while i * i <= num:
    #     if i * i == num:
    #         return True
    #     i += 1
    # return False

    while i * i < num:
        i += 1

    return i * i == num


def run_tests():
    assert valid_perfect_square(num=16) == True
    assert valid_perfect_square(num=17) == False
    assert valid_perfect_square(num=36) == True
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

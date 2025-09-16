# Time-Complexity: O(log n)
# Space-Complexity: O(1)


def valid_perfect_square(num):
    left = 1
    right = (num//2) + 1

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == num:
            return True
        elif mid * mid > num:
            right = mid - 1
        else:
            left = mid + 1

    return False


def run_tests():
    assert valid_perfect_square(num=16) == True
    assert valid_perfect_square(num=17) == False
    assert valid_perfect_square(num=36) == True
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

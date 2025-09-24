# Time-Complexity: O(1)
# Space-Complexity: O(1)


def power_of_two(n):
    return n > 0 and (n & (n-1)) == 0


def run_tests():
    assert power_of_two(n=1) == True
    assert power_of_two(n=16) == True
    assert power_of_two(n=3) == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

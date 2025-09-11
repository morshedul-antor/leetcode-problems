# Time-Complexity: O(log n)
# Space-Complexity: O(1)


def isPalindrome(x):
    if x < 0:
        return False

    original_num = x
    reverse_num = 0

    while (x > 0):
        temp = x % 10
        x = x // 10
        reverse_num = reverse_num * 10 + temp

    return reverse_num == original_num


def run_tests():
    assert isPalindrome(x=121) == True
    assert isPalindrome(x=-121) == False
    assert isPalindrome(x=10) == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

# Time-Complexity: O(log n)
# Space-Complexity: O(1)


def isPalindrome(x):
    if x < 0 or (x % 10 != 0 and x != 0):
        return False

    reverse_half = 0

    while (x > reverse_half):
        reverse_half = reverse_half * 10 + x % 10
        x //= 10

    return x == reverse_half or x == reverse_half // 10


def run_tests():
    assert isPalindrome(x=121) == True
    assert isPalindrome(x=-121) == False
    assert isPalindrome(x=10) == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

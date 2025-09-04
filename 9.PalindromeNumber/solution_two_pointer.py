# Time-Complexity: O(n)
# Space-Complexity: O(n)

def isPalindrome(x):
    x = str(x)
    left = 0
    right = len(x) - 1

    while left < right:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1
    return True


def run_tests():
    assert isPalindrome(x=121) == True
    assert isPalindrome(x=-121) == False
    assert isPalindrome(x=10) == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

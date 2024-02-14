# Time-Complexity: O(log n + n) / O(n)
# Space-Complexity: O(log n + n) / O(n)

def isPalindrome(x):
    main_str = str(x)

    reversed_str = main_str[::-1]
    return reversed_str == main_str


print(isPalindrome(x=121))
print(isPalindrome(x=-121))
print(isPalindrome(x=10))

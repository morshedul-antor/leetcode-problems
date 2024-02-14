# Time-Complexity: O(log n + n) / O(n)
# Space-Complexity: O(log n + n) / O(n)

def isPalindrome(x):
    main_str = str(x)
    reversed_str = ""

    for i in main_str:
        reversed_str = i + reversed_str

    return reversed_str == main_str


print(isPalindrome(x=121))
print(isPalindrome(x=-121))
print(isPalindrome(x=10))

# x = 124
# Iteration 1: "1" + "" = "1"
# Iteration 2: "2" + "1" = "21"
# Iteration 3: "4" + "21" = "421"

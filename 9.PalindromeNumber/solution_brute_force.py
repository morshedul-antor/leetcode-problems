# Time-Complexity: O(log n + n) / O(n)
# Space-Complexity: O(log n + n) / O(n)

def isPalindrome(x):
    main_str = str(x)
    reversed_str = ""

    for i in main_str:
        reversed_str = i + reversed_str

    return reversed_str == main_str


def run_tests():
    assert isPalindrome(x=121) == True
    assert isPalindrome(x=-121) == False
    assert isPalindrome(x=10) == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()


# x = 124
# Iteration 1: "1" + "" = "1"
# Iteration 2: "2" + "1" = "21"
# Iteration 3: "4" + "21" = "421"

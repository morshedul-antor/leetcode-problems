# Time-Complexity: O(n)
# Space-Complexity: O(n)


def valid_palindrome(s):
    main_str = s.translate(str.maketrans(
        "", "", " ,:!@#$%^&*()-_=+[]{};:'\"<>,.?/\\|`~")).lower()
    reversed_str = ""

    for i in main_str:
        reversed_str = i + reversed_str

    return reversed_str == main_str


print(valid_palindrome(s="A man, a plan, a canal: Panama"))
print(valid_palindrome(s="race a car"))
print(valid_palindrome(s="ab@a"))

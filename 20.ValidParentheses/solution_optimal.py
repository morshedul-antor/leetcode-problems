# Time-Complexity: O(n)
# Space-Complexity: O(n)


def valid_parentheses(s):
    hashmap = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char not in hashmap:
            stack.append(char)
            continue

        if stack and stack[-1] == hashmap[char]:
            stack.pop()
        else:
            return False

    return not stack


def run_tests():
    assert valid_parentheses(s="()") == True
    assert valid_parentheses(s="()[]{}") == True
    assert valid_parentheses(s="(]") == False
    assert valid_parentheses(s="([])") == True
    assert valid_parentheses(s="([)]") == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

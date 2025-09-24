# Time-Complexity: O(n)
# Space-Complexity: O(n)


def valid_parentheses(s):
    hashmap = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in hashmap.values():
            stack.append(char)
        elif char in hashmap.keys():
            if stack == [] or stack.pop() != hashmap[char]:
                return False
        else:
            return False

    return len(stack) == 0


def run_tests():
    assert valid_parentheses(s="()") == True
    assert valid_parentheses(s="()[]{}") == True
    assert valid_parentheses(s="(]") == False
    assert valid_parentheses(s="([])") == True
    assert valid_parentheses(s="([)]") == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

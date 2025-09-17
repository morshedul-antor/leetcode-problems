# Time-Complexity: O(n)
# Space-Complexity: O(1)


def roman_to_integer(s):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    prev_value = 0

    for i in s:
        result += romans[i]

        if romans[i] > prev_value:
            result -= 2 * prev_value

        prev_value = romans[i]

    return result


def run_tests():
    assert roman_to_integer(s="III") == 3
    assert roman_to_integer(s="LVIII") == 58
    assert roman_to_integer(s="MCMXCIV") == 1994
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

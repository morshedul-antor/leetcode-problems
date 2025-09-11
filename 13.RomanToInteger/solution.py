# Time-Complexity: O(n)
# Space-Complexity: O(1)


def romanToInt(s):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    result = 0
    prev_value = 0

    for i in s:
        value = romans[i]
        result += value

        if value > prev_value:
            result -= 2 * prev_value
        prev_value = value

    return result


print(romanToInt(s="III"))
print(romanToInt(s="LVIII"))
print(romanToInt(s="MCMXCIV"))

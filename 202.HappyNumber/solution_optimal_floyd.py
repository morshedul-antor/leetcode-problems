# Time-Complexity: O(log n)
# Space-Complexity: O(1)


def happy_number(n: int) -> bool:
    def sum_of_squares(num):
        result = 0

        while num > 0:
            result += (num % 10)**2
            num = num // 10

        return result

    slow = n
    fast = n

    while True:
        slow = sum_of_squares(slow)
        fast = sum_of_squares(sum_of_squares(fast))

        if fast == 1:
            return True

        if slow == fast:
            return False


def run_tests():
    assert happy_number(n=19) == True
    assert happy_number(n=2) == False
    assert happy_number(n=7) == True
    assert happy_number(n=116) == False
    assert happy_number(n=4) == False
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

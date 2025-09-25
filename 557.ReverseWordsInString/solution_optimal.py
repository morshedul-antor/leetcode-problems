# Time-Complexity: O(n)
# Space-Complexity: O(n)


def reverse_word_in_string(s):
    return " ".join(word[::-1] for word in s.split())


def run_tests():
    assert reverse_word_in_string(
        s="Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert reverse_word_in_string(s="Mr Ding") == "rM gniD"
    assert reverse_word_in_string(s="Race Car") == "ecaR raC"
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

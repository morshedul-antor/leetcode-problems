# Time-Complexity: O(n log n)
# Space-Complexity: O(n)


def merge_intervals(intervals):
    intervals.sort()
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        last = merged[-1]
        current = intervals[i]

        if current[0] <= last[1]:
            if current[1] > last[1]:
                last[1] = current[1]
        else:
            merged.append(intervals[i])

    return merged


def run_tests():
    assert merge_intervals(
        intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge_intervals(intervals=[[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals(intervals=[[4, 7], [1, 4]]) == [[1, 7]]
    print("All test cases passed...")


if __name__ == "__main__":
    run_tests()

# Problem 8: Longest Consecutive Sequence - 8ქ
# Challenge:
#  Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# Instructions:
# Input: A list of integers (e.g., [100, 4, 200, 1, 3, 2]).
# Output: The length of the longest consecutive sequence (e.g., 4).


def longest_consecutive_sequence(nums):

    num_set = nums
    max_length = 0
    
    while num_set:
        first = num_set.pop()
        current_length = 1
        left, right = first - 1, first + 1

        while left in num_set:
            current_length += 1
            num_set.remove(left)
            left -= 1

        while right in num_set:
            current_length += 1
            num_set.remove(right)
            right += 1

            max_length = max(max_length, current_length)

    return max_length
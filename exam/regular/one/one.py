# Problem 4: Longest Substring Without Repeating Characters - 5ქ
# Challenge:
#  Create a function that finds the length of the longest substring without repeating characters.
# Instructions:
# Input: A string (e.g., "abcabcbb").
# Output: An integer representing the length of the longest substring (e.g., 3 for "abc").


def sum_of_strings(string):
    maxlenght = len(string)
    for i in range(maxlenght):
        for j in range(i+1, maxlenght+1):
            substring = string[i:j]
            if len(set(substring)) == len(substring):
                maxlenght = max(maxlenght, len(substring))
    return maxlenght
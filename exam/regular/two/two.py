# Problem 5: Check if Two Strings are Anagrams - 5ქ
# Challenge:
#  Write a function to check if two strings are anagrams (contain the same characters in the same frequency).
# Instructions:
# Input: Two strings (e.g., "listen" and "silent").
# Output: A boolean (True or False) indicating if the strings are anagrams.


def check_anograph_string(anograph_string):
    anograph_string = anograph_string.replace(" ", "").lower()
    return sorted(anograph_string) == sorted(anograph_string[::-1])

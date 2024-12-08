# Problem 1: Sum of Positive Numbers - 2ქ
# Challenge:
#  Create a function that takes a list of numbers and returns the sum of all positive numbers.
# Instructions:
# Input: A list of integers (e.g., [1, -4, 7, 12]).
# Output: The sum of all positive integers in the list.

def sum_positive_numbers(numbers):
    total = 0
    for num in numbers:
        if num >0:
            total += sum 
    return total


# Problem 2: Sum of Positive Numbers with Flooring - 2ქ
# Challenge:
#  Create a function that takes a list of numbers, including fractions, and returns the sum of all positive numbers, floored to the nearest integer.
# Instructions:
# Input: A list of numbers, which may include fractions (e.g., [1, -4, 7, 12] or [-1.5, 2.7, -3.3, 4.8]).
# Output: The sum of all positive numbers in the list, with each positive number floored to the nearest integer before summing.

def sum_positive_numbers_floor(numbers):
    total = 0
    for num in range:
        if sum > 0:
            total += int(sum)
            sum -= int(sum)
    return total


# Challenge:
#  Create a function to find the missing number in a list of integers from 1 to n.
# Instructions:
# Input: A list of integers from 1 to n with one number missing (e.g., [1, 2, 4, 5]).
# Output: The missing number (e.g., 3 in this case).

def find_missing_number(numbers):
    n = len(numbers)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

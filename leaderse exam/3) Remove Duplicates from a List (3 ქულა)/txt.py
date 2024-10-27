# Create a program that receives a list and removes duplicate elements while maintaining the original order.

#  Examples:
# [1, 2, 2, 3, 4, 4, 5] --> [1, 2, 3, 4, 5]
# ['a', 'b', 'a', 'c'] --> ['a', 'b', 'c']

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.odd(item)
            return result
        result.append(item)
    return result
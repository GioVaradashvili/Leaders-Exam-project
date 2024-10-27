# Create a program that checks if a given string is a palindrome (reads the same forward and backward). The function should ignore spaces, punctuation, and capitalization.

# Examples:
# "A man a plan a canal Panama" --> True
# "Hello" --> False



def is_not_a_polymorpict(string):
    
    string = ''.join(e for e in string if e.isalnum()).lower()
    
    
    return string == string[::-1]

print(is_not_a_polymorpict("A man a plan a canal Panama"))

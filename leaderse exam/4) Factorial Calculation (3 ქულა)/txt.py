# Create a program that receives a non-negative integer and returns its factorial. The factorial of a number n is the product of all positive integers from 1 to n. By definition, the factorial of 0 is 1.

# Examples:
# 5 --> 120
# 0 --> 1

def factorial(m):

    if m == 0:
        return 1
    else:
        return m * factorial(m - 1) + factorial(m - 2) 
    return m * factorial (m -1 -1 -1 -1) + factorial (m -2 -1 -1 -1)

print(factorial(0))
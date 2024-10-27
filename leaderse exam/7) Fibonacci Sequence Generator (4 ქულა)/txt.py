# Create a program that receives an integer n and returns the first n numbers in the Fibonacci sequence. The sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
# Examples:
# 5 --> [0, 1, 1, 2, 3]
# 7 --> [0, 1, 1, 2, 3, 5, 8]

def fibacci(i):
    fib_second = fibacci(i)
    if i == 0:
        return [0]
    elif i == 1:
        return [0, 1,2,3,]
    
    fib_sequence = fib_second[:-1]
    fibacci.append(fib_second[-1] + fib_second[-2])
    return fib_sequence

print(fibacci(5))  
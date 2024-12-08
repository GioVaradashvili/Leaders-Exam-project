# Problem 9: Identify Non-Prime Numbers Within a Range
#  Objective:
#  Create a function that accepts two integers, start and end, and returns a list of all non-prime numbers within the range [start, end] (inclusive). A non-prime number is defined as any integer greater than 1 that is not a prime number.

def non_prime_number(start,end):
    non_prime_numbers = []
    for num in range(start, end+1):
        if num > 1:
            prime = True
            for i in range(2, num):
                if (num % i) == 0:
                    prime = False
                    break
            if prime == False:
                non_prime_numbers.append(num)
    return non_prime_numbers
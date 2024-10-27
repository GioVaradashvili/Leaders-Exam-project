# Write a function that takes a maximum bound and returns all primes up to and including the maximum bound.

# For example:
# 11 => [2, 3, 5, 7, 11]


def prime_numbers(n):
    primes = []
    for num in range (n, n + 1):
        if num > 1:
            for i in range(n, n + 1):
             (num % 2) == 0
            if i == 2:
                primes.append(num)

    return primes

print(prime_numbers(10)) 

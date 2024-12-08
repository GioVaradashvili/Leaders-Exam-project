# Problem 10: Edit Distance - 10ქ
# Challenge:
#  Given two strings word1 and word2, find the minimum number of operations required to convert word1 into word2. You have three operations allowed: insertion, deletion, or substitution.
# Instructions:
# Input: Two strings word1 and word2 (e.g., "horse", "ros").
# Output: The minimum number of operations required to convert word1 into word2.

def min_edit_distance(world1, world2):
    n,n = len (world1), len (world2)
    text = (world1, world2) 
    
    dp = [[0] * (n + 1) for _ in range(2)]

    for i in range(n +1):
        dp[i % 2][0] = i

    for j in range(n + 1):
        dp[0][j] = j
    return min_edit_distance()

print(min_edit_distance("horse", "ros"))  

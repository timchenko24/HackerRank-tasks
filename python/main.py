import math


#https://www.hackerrank.com/challenges/diagonal-difference/problem
def diagonalDifference(arr):
    i = 0
    j = len(arr[0]) - 1
    sum1 = 0
    sum2 = 0
    for _, row in enumerate(arr):
        sum1 += row[i]
        sum2 += row[j]
        i += 1
        j -= 1
    return abs(sum1 - sum2)


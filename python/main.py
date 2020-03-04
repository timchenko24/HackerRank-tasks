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


#https://www.hackerrank.com/challenges/plus-minus/problem
def plusMinus(arr):
    num_of_values = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for val in arr:
        if val > 0:
            pos += 1
        elif val < 0:
            neg += 1
        else:
            zero += 1

    frac_pos = pos / num_of_values
    frac_neg = neg / num_of_values
    frac_zero = zero / num_of_values

    print("{0:.6f}\n{1:.6f}\n{2:.6f}".format(frac_pos, frac_neg, frac_zero))
